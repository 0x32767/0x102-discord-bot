let commandSet = require("./lib/BotCommands");
let commands = new commandSet.commandSet();


commands.add("/kill <user:User>", (function (ctx, args) {
    ctx.send(`${args.user} was burned to a crisp by ${ctx.invoker}`);
}),);


commands.add("/revive <user:User>", (function (ctx, args) {
    ctx.send(`${args.user} was given a totem of undying  by ${ctx.invoker}`);
}),);


module.exports = commands;
