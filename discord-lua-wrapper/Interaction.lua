--[[
    Instrad of using the discord.py interaction, which contains methord for deleting and banning users,
    I have created a new class that contains methods for interacting with the discord.py library. This
    class should also hopefully stop injections from happening.
]]--

function createInteraction(Interaction)
    return {
        ["user"] = {
            ["name"] = tostring(Interaction.user.name),
            ["avatar"] = tostring(Interaction.user.avatar),
            ["id"] = tonumber(Interaction.user.id),
        },
        ["server"] = {
            ["name"] = tostring(Interaction.server.name),
            ["id"] = tonumber(Interaction.server.id),
        },
        ["channel"] = {
            ["name"] = tostring(Interaction.channel.name),
            ["id"] = tonumber(Interaction.channel.id),
        }
    }
end
