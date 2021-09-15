

const baseurl = "https://dog.ceo/api/breeds/image/random";


const mybtn = document.getElementById("getJockBtn")


mybtn.addEventListener("click", () => {

    document.getElementById("myHiTagAll").innerHTML = null

    const responsePromis = fetch(baseurl)
    console.log('responsePromis:', responsePromis)

    responsePromis.then(shivam => { return shivam.json() })
        .then((response) => {
            let img = document.createElement("img")
            img.setAttribute("src", response.message)
            document.getElementById("myHiTag").append(img)
        })

    responsePromis.catch(() => {
        console.log("Rejected Request");
    })

})

const mybtnAll = document.getElementById("getJockBtnAll")

mybtnAll.addEventListener("click", () => {

    document.getElementById("myHiTagAll").innerHTML = null
    document.getElementById("myHiTag").innerHTML = null

    const responsePromis = fetch(baseurl)
    console.log('responsePromis:', responsePromis)

    responsePromis.then(shivam => { return shivam.json() })
        .then((response) => {
            let img = document.createElement("img")
            img.setAttribute("src", response.message)
            document.getElementById("myHiTagAll").append(img)
        })

    responsePromis.catch(() => {
        console.log("Rejected Request");
    })

})

