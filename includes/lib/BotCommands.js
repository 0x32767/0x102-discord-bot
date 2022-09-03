class commandSet {
    constructor() {
        this.commands = {};
    }

    add(name, command, desc) {
        if (desc === undefined) {
            desc = "...";
        }
        if (name === undefined) {
            console.error("Error: command was not given a name");
            return;
        }
        if (command === undefined) {
            console.error(`Error: command ${name} was never given a body`);
            return;
        }

        this.commands[name] = { cmd: command, desc: desc }
    }
}

module.exports = { commandSet };
