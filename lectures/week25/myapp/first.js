
const express = require("express");


const app = express();

const PORT = 3003;

app.use(express.urlencoded({ extended: true }))

app.get("/", (req, res) => {
    res.sendFile(`${__dirname}/views/home.html`)
})


app.get("/survey", (req, res) => {
    res.sendFile(`${__dirname}/views/survey.html`)
})

app.get("/signup", (req, res) => {
    res.sendFile(`${__dirname}/views/signup.html`)
})


app.get("/survey/submit", (req, res) => {
    res.send(`<h1>Your Nmae Is: ${req.query.name} </h1> <h1>Your Email Is: ${req.query.email}</h1> <h1>Your Password Is: ${req.query.password} </h1> <h1>Your Address Is: ${req.query.address} </h1> <h1>Your City Is: ${req.query.city} </h1> <h1>Your Zip Is: ${req.query.zip}</h1>`)
})


app.post("/signup/submit", (req, res) => {
    res.send(`<h1>Your Password Is: ${req.body.email}</h1> <h1>Your Email Is: ${req.body.password}</h1> `)
})



app.get("*", (req, res) => {
    res.sendFile(`${__dirname}/views/notfound.html`)
})

app.listen(PORT, () => {
    console.log("Listing Port 3003");
})



