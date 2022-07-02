embed = {
    ["title"] = nil,
    ["description"] = nil,
    ["url"] = nil,
    ["color"] = nil,
    ["timestamp"] = nil,
    ["footer"] = nil,
    ["image"] = nil,
    ["thumbnail"] = nil,
    ["author"] = nil,
    ["fields"] = {
        {
            ["name"] = nil,
            ["value"] = nil,
            ["inline"] = nil
        }
    }
}

function embed:add_field(name, value, inline)
    self.fields[#self.fields + 1] = {
        ["name"] = name,
        ["value"] = value,
        ["inline"] = inline
    }
    return self
end
