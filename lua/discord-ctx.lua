ctx = {
    ["channel"] = nil,
    ["args"] = {},
    ["user"] = nil
}

function ctx:send(message, embed)
    self:channel():send(message, embed)
end
