# Custom commands docs


## Intro

The documentation assumes that you have a basic understanding of lua or general programing.

<hr>

## Command syntax

<hr>

All lua commands that you want to execute need to be anonymous and take an argument, this is because of the way that the python `lupa` module works.


> ### Parameters for `ctx.response.send_embed`

> title

type: string

The title of you embed.

> description

type: string

The description for you embed.

> fields

type: array/list of table/hash-map/dict

example:
```lua
fields={
    {
        ["name"]="field name",
        ["value"]="value of field"
        ["inline"]=true or false
    }
}
```

> footer

type: string

Your embed footer text.

> color

type: hex integer, any hex color value (use a color picker)

The color of the embed.

<br>

> #### Example

```lua
function (ctx)
    return ctx.response.send_embed{
        title="I'm an embed",
        description="...",
        fields={
            {
                ["name"] = "...",
                ["value"] = "...",
                ["inline"] = true
            }
        },
        footer="...",
        color=0x000
    }
end
```

> ### Parameters for `ctx.response.send_message`

> content

type: string

The message you want to send when the command is run.

#### Example

```lua
function (ctx)
    return ctx.response.send_message("hi")
end
```

<hr>

## The waiting list

Because anyone can upload a custom command things would get very messy very quickly if a command was uploaded instantly and could be used at the time of upload. Therefor a waiting list has been put in place to stop a massive flood like this from happening.

When your command is submitted (via discord or a pull request) it is not instantly put in place and runnable. Your command will instead be put in a waiting list (found here https://github.com/0x32767/0x102-discord-bot/tree/master/docs/waiting-list.rst). Your command will be either (approved or denied).

No user information is stored at all (you can dive into the code if you want) so users who have had their command denied may need to rewrite them or contact me, via discord (0x32#0293).


## Published commands

All commands are open source with no exceptions, the source of the commands can be seen with `/inspectcommand >>INSERT COMMAND NAME HERE<<`. This is so that server owners and users can see what the command does before actually running it.

Published commands can then only be changed through private contact or a pull request. Commands can also be deleted if the user wants them to free of hassle.
