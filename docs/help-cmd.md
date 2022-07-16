# The 0x102 discord bot help command.

## Intro

Hello, if you are a new user and would like to get started then this is the place for you, 0x102 is a discord bot packed full of new features and is being updated by it's developer, 0x102 also syncs with other discord bots that have also just started such as the Arty serries of bots. Together these bots provide a powerful and easy to use collection of bots that can truly take your server to the next level.

## Cogs
<hr>
Cogs are used to organize commands that are related.


## Apis

The `apis` cog is a wrapper for all the commands that interact with apis, these apis are large public databases of which some are free and some are payed, these databases can store thousands of trivia questions, images of cats, dogs, ech...


### /fox

>Usage:

`/fox`

This command will send a picture of a fox.

### /dog

>Usage:

`/dog`

This command is like the `/cat` command and will send a random picture of a dog.

### /cat

>Usage:

`/cat`

This command is like the `/dog` command and will send a random picture of a cat.

### /meme

>Usage:

`/meme`

This command is like the `/cat` command but will send a quality random meme.

### /catfact

>Usage:

`/catfact`

This command will send a random fact about cats, could get interesting...

### /dogfact

>Usage:

`/dogfact`

This command will send a random fat about dogs, could use these to cheat on the trivia command.

## Decrypt

This command can be used to crack caesar ciphers and two other forms of encryption.

### /decrypt

>Usage:

`/decrypt <msg>`

- msg: The message you want to decrypt.

This command can be used to crack caesar ciphers and two other forms of encryption supported by the bot.

## Encrypt

>Usage:

`/encrypt <msg>`

- msg: The message you want to encrypt.

This command will give you three options to encrypt your message:
 - hexadecimal encode
 - caesar cipher
 - binary encode

## Github api

Github is a platform where you can see the source code of a program, you'r in github right now, viewing this, (do feel free to look at the source code of the bot :^) ). This cog allows you to see some info about a github user.

### /getuser

>Usage:

`/getuser <username>`

- username: a github username, like `0x32767`

This gets some information about a github user.

### /getrepos

>Usage:

`/getrepos <username>`

- username: a github username

This gets a list of the github user's github repos.

## Lua commands

Custom commands can be created in lua and then run by 0x102.

### /runcommand

>Usage:

`/runcommand <name>`

- name: the name of the command you want to run

This command runs a command that was created by a user such a yourself.

### /inspectcommand

>Usage:

`/inspectcommand <name>`

- name: the name of the command you want to inspect

This command will send the source code of the command, this was made so you know what the command is doing before you run it.

### /newcommand

>Usage:

1. create a message with th the code of your command.

2. run `/newcommand <name>`

   - name: the name of your command.

## Minecraft

This cog can be used to look up important minecraft things.

### /mcidlookup

> Usage:

`/mcidlookup <id>`

- id: the id of the block you want to find
