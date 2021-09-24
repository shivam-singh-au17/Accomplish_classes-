const http = require("http")

function handler() {
    console.log("some http req");
}

const server = http.createServer(handler)
const PORT = 3001

server.listen(PORT, () => {
    console.log("Listing Port 3001");
})