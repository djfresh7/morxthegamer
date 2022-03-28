const express = require("express");
const fs = require("fs")
const app = express();

app.get("/", (req, res) => {
  fs.readFile("index.html", "utf-8", (e, d) => {
    if (e) return;
    res.send(d);
  });
});
  
function listens() {
  app.listen(8000, () => console.log("Server is RUNNING...\nThe BOT has started..."));
}

module.exports = { listens }