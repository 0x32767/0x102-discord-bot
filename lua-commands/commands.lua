--[[
    This command can be used to check if custom commands are working correctely.
]]--
function ping(ctx)
    return ctx.response.send_message("pong!")
end
