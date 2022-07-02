discord = require("discord-lib")

discord.on("/test", function(ctx)
    ctx:send{embed=discord.newEmbed{
        title="Test",
        description="This is a test"
    }}
end)

discord.on("/echo", function (ctx, arg)
    ctx:send(arg)
end)
