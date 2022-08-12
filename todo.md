# The list

| status                  | id    | title            | link     |
| ----------------------- | ----- | ---------------- | -------- |
| :black_square_button:   | #0001 | Github Api       | [href]() |
| :black_square_button:   | #0002 | Server Telephone | [href]() |
| :black_square_button:   | #0003 | Spam detection   | [href]() |
| :x:                     | #0004 | Message logs     | [href]() |
| :black_square_button:   | #0005 | reputation       | [href]() |
| :black_square_button:   | #0006 | gamboling        | [href]() |
| :x:                     | #0007 | profanity        | [href]() |
| :repeat:                | #0008 | Bot syncing      | [href]() |
| :black_square_button:   | #0009 | Some website     | [href]() |
| :ballot_box_with_check: | #000a | custom commands  | [href]() |
| :repeat:                | #000b | edit commands    | [href]() |
| :repeat:                | #000c | run commands     | [href]() |
| :repeat:                | #000d | delete commands  | [href]() |
| :ballot_box_with_check: | #000e | error logging    | [href]() |
| :white_check_mark:      | #000f | encryption       | [href]() |
| :white_check_mark:      | #0010 | decryption       | [href]() |
| :black_square_button:   | #0011 | optimize         | [href]() |
| :black_square_button:   | #0012 | Sokoban          | [href]() |
| :black_square_button:   | #0013 | 4 in a row       | [href]() |
| :black_square_button:   | #0014 | Tetris           | [href]() |
| :black_square_button:   | #0015 | rick rolling     | [href]() |
| :black_square_button:   | #0016 | dank memer api   | [href]() |
| :black_square_button:   | #0017 | text adventure   | [href]() |
| :black_square_button:   | #0018 | activities       | [href]() |

# More details

## Github Api

Github has an api that lets you see some basic information about a github user or repo. This feature has been implemented to an extent, but is not yet complete.

Status: **delayed**

Expected to be implemented: ==soon==

## Server Telephone

This feature should allow to people from different servers to communicate with each other. This feature has not been started.

Status: **not started**

Expected to be implemented: ==soon==

## Spam detection

This will look at the average time between messages sent by a user and see if they are over a threshold. This feature was under development but after discord made `MESSAGE_CONTENT` a privilege, the feature was put on hold.
The algorithm would have worked by also checking the message content, to assure that the user is deliberately spamming. However, the announcement put the feature on hold.

Status: **working now**

Expected to be implemented: ==week==

## Message logs

This shares the same problem that the spam detection has. The idea is to log all deleted massages in a channel, but messages are deleted for a purpose, and if a message contains sensitive information, it should not be logged. Put simply: messages would have been deleted for a reason and should not be logged.

Status: **may/may not be coming**

Expected to be implemented: ==never==

## Reputation

This feature would be more of an in-server currency that would give users privileges to do stuff. However, if the bot grows large then there would be a problem as to were to store the reputation of each user and other stuff (e.g other currencies). Using the bot should not require payment, but if the feature becomes desired then servers who have over 1,000 users with this feature on will need to pay for use. I would also prefer to use a machine dedicated to databases than a general purpose computer.

Status: **not started**

Expected to be implemented: ==soon==

## Gamboling

This feature would allow a user to gamble a part of their reputation. This would be a good way to get some extra reputation and teach people not to gamble in the real world. This would have to be made after the reputation feature is implemented so that there is a reward and penalty for winning\losing.

Status: **not started**

Expected to be implemented: ==after Reputation==

## Profanity

Profanity is one thing that most server owners don't want in their servers, besides nsfw channels. Although discord does not allow users under 13 to register, some still do. This feature is not designed to to keep users under 13 from using profanity, but to provide a more clean environment in general. Again this was being just before the announcement and was therefor put on hold due to the `MESSAGE_CONTENT` problem. Instead a reporting feature would be added.

Status: **delayed**

Expected to be implemented: ==soon==

## Bot syncing

0x102 has partnered with `Arty-Studios` to create a network of bots. This network would just improve the bot experience because reputation progress would be distributed across the network.

Status: **working on it**

Expected to be implemented: ==soon==

## Some website

The website would be similar to https://www.dankmemer.lol/ or https://mee6.xyz/ but with a few extra features. The website would be made with php or django. This website would contain bots that were created from the ArtyStudios and 0x102. The website would also have an api, and also an integrated text editor for lua (for custom commands).

Status: **paused**

Expected to be implemented: ==soon==

# Custom commands

Custom commands are very important to all bots that have them. They allow users to customize the bot to their liking. This feature is still under development and has many restrictions. Custom commands are written in lua, because it is a beginner friendly language. For more experienced programers forcing lua can seem restricting, therefor there will be an aim to include support for any language that can compile to a .pyc file ( ).

# what / why a \*.pyc file?

Cpython (the c implementation of python) is compiled to bytecode stored in a .pyc file. Functions can still be called from this file, so if you were to convert a c++ function to a python bytecode, then you could call it from python (the same applies to any language not just c++). I will try again to create a compiler for this feature. But I will not be able to convert all languages to pyc. I would really appreciate it if some one made a compiler.
