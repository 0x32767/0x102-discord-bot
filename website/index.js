const express = require("express");
let app = express()


app.get("/", function (req, res) {
    res.render("index.ejs")
});

app.listen(3000, function () {
    console.log("http://127.0.0.1:3000")
})
