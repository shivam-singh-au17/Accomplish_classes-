
let btn = document.getElementById("myBtn")
let res = document.getElementById("result")

btn.addEventListener("click", () => {

    let strValue = document.getElementById("myString").value
    let store = ""
    for (let i = 0; i < strValue.length; i++) {
        if (strValue[i] != "#") {
            store += strValue[i]
        }
    }
    let p = document.createElement("p")
    p.innerText = store
    res.append(p)

})

