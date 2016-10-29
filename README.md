# wakamon

Archives [wakatime] daily statistics of the last week to MongoDB. Use with `cron` or timers for fun and profit.

Quickstart via:

```
docker run --rm --name wakamon \
    -e API_KEY="your-api-key" \
    -e MONGO_CONNECTION_STRING="mongodb://server:27017/" \
    sunside/wakamon:latest
```

or with linked `mongodb` containers:

```
docker run --rm --name wakamon \
    --link mongodb:db \
    -e API_KEY="your-api-key" \
    -e MONGO_CONNECTION_STRING="mongodb://db:27017/" \
    sunside/wakamon:latest
```

Supported environment variables are:

* `API_KEY`: Your wakatime API key (required)
* `MONGO_CONNECTION_STRING`: Your MongoDB connection string (required)
* `MONGO_DB`: The MongoDB database to use (optional)
* `MONGO_COLLECTION`: The MongoDB collection to use (optional)

[wakatime]: https://wakatime.com/
