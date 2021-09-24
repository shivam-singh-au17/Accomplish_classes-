const http = require("http")

const server = http.createServer((req, res) => {
    
    let count = 0
    if (req.url == "/") {
        res.write(`<h1>Times Visited: ${count}</h1>`);
        res.end()
    } else if (req.url == "/reset") {
        res.write(`<h1>Reset Successful</h1>`)
        res.end()
    }
    count = count + 1;
})

const PORT = 3001;

server.listen(PORT, () => {
    console.log("Listing Port 3001");
})