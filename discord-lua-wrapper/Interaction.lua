--[[
    Instrad of using the discord.py interaction, which contains methord for deleting and banning users,
    I have created a new class that contains methods for interacting with the discord.py library. This
    class should also hopefully stop injections from happening.
]]--

function (Interaction)
    return {
        ["user"] = {
            ["name"] = tostring(Interaction.user.name),
            ["avatar"] = tostring(Interaction.user.avatar),
            ["id"] = tonumber(Interaction.user.id),
        },
        ["server"] = {
            ["name"] = tostring(Interaction.guild.name),
            ["id"] = tonumber(Interaction.guild.id),
        },
        ["channel"] = {
            ["name"] = tostring(Interaction.channel.name),
            ["id"] = tonumber(Interaction.channel.id),
        },
        --[[
            Thse tables are going to be returned so that python can inspect it instead of
            sending the messages directely (a caouse for utter disaster)
        ]]--
        ["response"] = {
            ["send_embed"] = function (title, description, fields, footer, color)
                return {
                    ["type"] = "emb",
                    ["object"] = {
                        ["title"] = title,
                        ["description"] = description,
                        ["fields"] = fields,
                        ["footer"] = footer,
                        ["color"] = color
                    }
                }
            end,
            ["send_message"] = function (msg, hidden)
                return {
                    ["type"] = "msg",
                    ["object"] = {
                        ["content"] = msg,
                        ["ephemeral"] = hidden
                    }
                }
            end
        }
    }
end
