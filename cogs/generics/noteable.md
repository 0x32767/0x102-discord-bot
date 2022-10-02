# HOW-THIS-IS-A-COMMAND----

## Intro

Commands in discord.py can have alices, this does mean that to get the alies that was used you can use the Context.invoked_with property. This means that we can have multiple commands within a single function, this however, does not work with slash commands which is why I will be using the commands.command decorator. The inability to use slash commands does make up for the little boiler plate this methord does use.

## workings

This file contains a dict with keys as strings and lists of strings as values. I will itterate over all the keys and use them as command alieses, then I will open the dict again and look for the alies the command was invoked with this I will get the value associated with the command aliece. Now that we have the list we will pick one item from that list and send it. This will lead to verry litte boiler plate and is why I have chosen to use it.
