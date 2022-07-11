--[[
    This is a message class that contains methods for interacting with the discord.py library.
]]--


function newMessage(content)
    return {
        ["type"] = "message",
        ["content"] = content
    }
end
