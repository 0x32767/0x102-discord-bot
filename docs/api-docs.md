# Sync api

> btw

This api is designed to sync settings across multiple discord bots.

## Settings

| Key          | usage                             | example                                                   |
| ------------ | --------------------------------- | --------------------------------------------------------- |
| whitelisting | allow whitelisting system         | `use_whitelisting_enabled` or `use_whitelisting_disabled` |
| blacklisting | allow blacklisting system         | `use_blacklisting_enabled` or `use_blacklisting_disabled` |
| allow_links  | removes all server links          | `allow_links_enabled` or `allow_links_disabled`           |
| spam_mod     | auto punish users for spamming    | `spam_mod_enabled` or `spam_mod disabled`                 |
| auto_mod     | Detect profanity and report it.   | `auto_mod_enabled` or `auto_mod_disabled`                 |
| logging      | log all messages                  | `logging_enabled` or `logging_disabled`                   |
| run_cc       | If users can run custom commands. | `run_cc_enabled` or `run_cc_disabled`                     |
| reputation   | User server reputation system.    | `reputation_enabled` or `reputation_disabled`             |

## Api Design

Hello, this is a place where the api will be documented, pull requests by the api owner and other people can contribute, to either fix spelling mistakes or to create suggestions optimize the api or use of said api.

### SQL tables

The api should consist of several tables, each table should serve a unique purpose to optimize disk usage.

#### `settings`

This table should have the following columns:

| db_identifier | guild_id | enum(>>INSERT-EXAMPLES-FROM-SETTINGS-HERE<<)          |
| ------------- | -------- | ----------------------------------------------------- |
| 1a2b3c4d5e6f  | 1234567  | {1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1}                     |
| ............  | .......  | {..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 1} |

This table should have the guild_id and an enum at the minimum.

#### `updates`

This table should have the following columns:

| db_identifier | guild_id | updated |
| ------------- | -------- | ------- |
| 1a2b3c4d5e6f  | 1234567  | 1       |
| ............  | .......  | ....... |

This table has the guild_id and the updated column. The updated column is if the settings have been updated in the last half hour. The updated column should be reset to `0` every half hour too.
