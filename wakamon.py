from pymongo import MongoClient
from datetime import datetime, date, timedelta
import json
import httplib2
import os

# wakatime uses Let's Encrypt which is not natively supported by httplib2
system_ca_file = os.getenv('CA_FILE', '/etc/ssl/certs/ca-certificates.crt')

# wakatime API key
api_key = os.environ.get('API_KEY')
if api_key is None:
    print('Missing API_KEY environment variable.')
    exit(1)

# MongoDB connection string
connection_string = os.environ.get('MONGO_CONNECTION_STRING')
if connection_string is None:
    print('Missing MONGO_CONNECTION_STRING environment variable.')
    exit(1)

# Database and collection configuration
db = os.getenv('MONGO_DB', 'wakatime')
collection = os.getenv('MONGO_COLLECTION', 'summaries')

# the summaries endpoint
today = date.today().strftime("%Y-%m-%d")
one_week_ago = (date.today() - timedelta(days=7)).strftime("%Y-%m-%d")
endpoint = 'https://wakatime.com/api/v1/users/current/summaries?start=%s&end=%s&api_key=%s' % (one_week_ago, today, api_key)

h = httplib2.Http(".cache", ca_certs=system_ca_file)

print('Fetching data ...')
(resp_headers, content) = h.request(endpoint, 'GET')

if resp_headers.status >= 300:
    print('HTTP request failed with status code %s' % resp_headers.status)
    exit(1)

print('Archiving summaries ...')
client = MongoClient(connection_string)
db = client[db]
collection = db[collection]

summaries = json.loads(content)
for datum in summaries['data']:
    date = datum['range']['date']
    id = datetime.strptime(date, '%Y-%m-%d')
    datum['_id'] = id
    collection.replace_one({'_id': id}, datum, upsert=True)
