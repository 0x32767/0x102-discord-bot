const express = require("express");
const fs = require("fs");


let app = express();

app.set("view engine", "ejs");
app.use(express.json());
app.use(express.urlencoded({extended: true}));


data = {}


app.get("/", function(req, res)
{
    res.redirect("https://github.com/0x32767/0x102-discord-bot");
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
