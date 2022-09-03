# Includes

A new part of my bot is going to be introducing the ability to work on the bot with other languages,this would include:

- perl
- java script
- php

This is possible with the power of the bond module.

## JS Integration

A new part of my bot will be the ability to create custom commands in js, JS and python are both the most popular languages. JS also has some features such as being able to import directly from json and the ease of anonymous functions.

### Use

I have done my best to remove as much boiler plate as possible when creating the api.

```js
let commandSet = require("./lib/BotCommands");
let commands = new commandSet.commandSet();

// code goes here

module.exports = commands;
```

We start by importing the module and then creating a new `commandSet` class. This is similar to the express module where you directly add functions with the `add` method. This is an example:

```js
commands.add(
  "/cmd_name",
  function (ctx, args) {
    ctx.send("this is my response");
  },
  "description"
);
```

The first param is the command name and can be prefixed with a `/`, next is an anonymous function that takes a ctx and args param. The ctx is the command context and is similar to the discord.py command context. The args param is a json object with any passed values.

```js
module.exports = commands;
```

we finally add this line so that python can get easy access to it. And that is all.
