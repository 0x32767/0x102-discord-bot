--[[
    The following functuon creates an embed class
]]--


function createEmbed(title, description, footer)
    return {
        ["type"] = "embed",
        ["title"] = title,
        ["description"] = description,
        ["color"] = 0x00ff00,
        ["fields"] = {},
        ["footer"] = {
            ["text"] = footer
        },
        ["addField"] = function(self, name, value)
            table.insert(self.fields, {
                ["name"] = name,
                ["value"] = value
            })
        end
    }
end
