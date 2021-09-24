const express = require("express");
const app = express()

const PORT = 3001;
let count = 0;

app.get("/", (req, res) => {

    count++;
    res.send(`<h1>Times Visited: ${count}</h1>`);
    
})


app.get("/reset", (req, res) => {

    res.send(`<h1>Reset Successful</h1>`);
    count = 0;

})


app.listen(PORT, () => {
    console.log("Listing Port 3001");
})