embed = require("discord-embed")


function table.coppy(org)
    local new = {}
    for k, v in pairs(org) do
        new[k] = v
    end
    return new
end


discord = {
    ["commands"] = {}
}


function discord:newEmbed(title, description, url, color, timestamp, footer, image, thumbnail, author)
    local embed = table.coppy(embed)
    embed.description = description
    embed.timestamp = timestamp
    embed.thumbnail = thumbnail
    embed.footer = footer
    embed.author = author
    embed.title = title
    embed.color = color
    embed.image = image
    embed.url = url
    return embed
end

function discord:on(name, func)
    self.commands[name] = func
end
