const express = require("express")
const app = express()
const fs = require("fs")

app.get("/", (rq,rs) => {
  fs.readFile("serv.html", { encoding: "utf-8" }, (e,d) => {
    rs.send(d);
  })
})

function listening() {
  app.listen(6000, () => {
    console.log("Running the Mod Bot...")
  })
}

module.exports = { listening }