const express = require("express");
const sqlite3 = require("sqlite3");


let app = express();

app.set("view engine", "ejs");
app.use(express.json());
app.use(express.urlencoded({extended: true}));


const links = {
    0: "https://raw.githubusercontent.com/0x32767/0x102-discord-bot/master/",
}
let data = {}

app.get("/", function(req, res)
{
    res.render("index", cards=[
        {
            title: "0x102",
            text: "A general purpose discord bot",
            id: 0
        }
    ])
});


app.get("/lua/form", function(req, res)
{
    res.render("lua-form.ejs");
});


app.get("/card/:id", function(req, res)
{
    res.render("card", info={link: links[req.params.id]});
});


app.post("/lua/code/", function(req, res)
{
    let code = req.body.code;
    let id = req.body.id;
    let db = new sqlite3.Database("D:\\programing\\0x102-discord-bot\\commands.db");
    db.run("INSERT INTO lua_code (id, code) VALUES (?, ?)", [id, code]);
    db.close();
    res.send({success: true});
});


app.post("/api/db/update", function(req, res)
{
    let inf = data[req.body["server-id"]];
    switch (req.body["__type__"])
    {
        case "get":
            res.send(
                {
                "server-id": req.body["server-id"],
                "server-settings": {
                    "auto-spam": inf["auto-spam"],
                    "spam-tolerance": inf["spam-tolerance"],
                    "profanity-filter": inf["profanity-filter"],
                    "max-warnings": inf["max-warnings"]
                },
                "__type__": "response"
                }
            );
            break;

        case "update":
            for (let key in req.body.keys())
            {
                data[req.body["server-id"]][key] = req.body[key];
            }
            res.send(
            {
                "server-id": req.body["server-id"],
                "server-settings": {
                    "auto-spam": inf["auto-spam"],
                    "spam-tolerance": inf["spam-tolerance"],
                    "profanity-filter": inf["profanity-filter"],
                    "max-warnings": inf["max-warnings"]
                },
                "__type__": "response"
            });
            break;

        default:
            res.send(
            {
                "server-id": req.body["server-id"],
                "error": `Invalid type ${req.body["type"]}`,
                "status": "heard",
                "__type__": "response"
            });
            break;
    }

    res.send({status: 200});
});


app.listen(3000, function()
{
    console.log("http://localhost:3000/");
});
