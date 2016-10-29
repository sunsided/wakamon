# wakamon

Archives [wakatime] daily statistics to MongoDB.

Quickstart via:

```
docker run --rm --name wakamon \
    -e API_KEY="your-api-key" \
    -e MONGO_CONNECTION_STRING="mongo://server:27017/" \
    wakamon:latest
```

or with linked `mongodb` containers:

```
docker run --rm --name wakamon \
    --link mongodb:db
    -e API_KEY="your-api-key" \
    -e MONGO_CONNECTION_STRING="mongo://db:27017/" \
    wakamon:latest
```

Supported environment variables are:

* `API_KEY`: Your wakatime API key (required)
* `MONGO_CONNECTION_STRING`: Your MongoDB connection string (required)
* `MONGO_DB`: The MongoDB database to use (optional)
* `MONGO_COLLECTION`: The MongoDB collection to use (optional)

[wakatime]: https://wakatime.com/