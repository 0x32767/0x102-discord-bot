># 0x102 discord bot api requirements


<br>

>## overview

<br>

The plan is that all discord bots that we (another developer) will created will use a web api to store server settings. These settings will be stored in a database of some description, and user data can be stored in a caching database, i.e redis.

<br>

>## api setup

<br>

This api will be private and will require a token to access. Information will be stored in the following table format:

```sql
CREATE TABLE server_settings (
    server_id BIGINT UNSIGNED NOT NULL,
    auto_spam BOOLEAN NOT NULL DEFAULT TRUE,
    spam_tolerance INTEGER NOT NULL DEFAULT 5,
    profanity_filter BOOLEAN NOT NULL DEFAULT TRUE,
    max_warnings INTEGER NOT NULL DEFAULT 3
);
```

`server_id`: The id of the discord server.

`auto_spam`: Whether or not the bot will automatically spam the server.

`spam_tolerance`: The amount of messages that a user can send before the bot will flag up that they are spamming. (msgs per 10 seconds)

`profanity_filter`: Whether or not the bot will filter profanity.

`max_warnings`: The amount of warnings a user can have before the bot will kick them.

<br>

>### calling from api

<br>

The below is an example of an api call:

```json
{
    "server-id": INSERT-SERVER-ID-HERE,
    "__type__": "get",
    "token": "some token"
}
```

This call should get the following response:

```json
{
    "server-id": INSERT-SERVER-ID-HERE,
    "server-settings": {
        "auto-spam": true,
        "spam-tolerance": 5,
        "profanity-filter": true,
        "max-warnings": 3
    },
    "__type__": "response",
}
//  this would be the response of  server with default settings
```

<br>

>### updating api

<br>

A update request should look like this:

```json
{
    "server-id": INSERT-SERVER-ID-HERE,
    "token": "some token",
    "server-settings": {
        "spam-tolerance": 10
    },
    "__type__": "update",
}
// only things that are going to change should be in this api call, this should hopefully not require two api calls, (one to get, one to update)
```

A response would be a generic response like this (as if it were a separate api call):

```json
{
    "server-id": INSERT-SERVER-ID-HERE,
    "server-settings": {
        "auto-spam": true,
        "spam-tolerance": 10,
        "profanity-filter": true,
        "max-warnings": 3
    },
    "__type__": "response"
}
```
