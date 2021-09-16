
const myData1 = document.getElementById("globalData1")
const myData2 = document.getElementById("globalData2")

function showData(arr) {
    arr.forEach(item => {
        let trEl = document.createElement("tr");
        let tdEl1 = document.createElement("td");
        tdEl1.innerText = item.id;
        let tdEl2 = document.createElement("td");
        tdEl2.innerText = item.userId;
        let tdEl3 = document.createElement("td");
        tdEl3.innerText = item.title;
        let tdEl4 = document.createElement("td");
        tdEl4.innerText = item.body;
        trEl.append(tdEl1, tdEl2, tdEl3, tdEl4);
        document.getElementById("myHiTag").append(trEl)
    });
}

function showData2(item) {
    let trEl = document.createElement("tr");
    let tdEl1 = document.createElement("td");
    tdEl1.innerText = item.id;
    let tdEl2 = document.createElement("td");
    tdEl2.innerText = item.userId;
    let tdEl3 = document.createElement("td");
    tdEl3.innerText = item.title;
    let tdEl4 = document.createElement("td");
    tdEl4.innerText = item.body;
    trEl.append(tdEl1, tdEl2, tdEl3, tdEl4);
    document.getElementById("myHiTag").append(trEl)

}

async function getData(nameValue) {

    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/posts/?userId=${nameValue}`)
        const jsonData = await response.json()
        showData(jsonData)

    }
    catch (e) {
        return e.message
    }
}

async function getData2(nameValue2) {

    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${nameValue2}`)
        const jsonData = await response.json()
        showData2(jsonData)

    }
    catch (e) {
        return e.message
    }
}

async function getData3() {

    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/posts/`)
        const jsonData = await response.json()
        showData(jsonData)

    }
    catch (e) {
        return e.message
    }
}


myData1.addEventListener("input", (e) => {

    myData2.value = null

    document.getElementById("myHiTag").innerHTML = null

    const nameValue = e.target.value;
    if (nameValue.length == 0) {
        getData3()
    }
    getData(nameValue)

})

myData2.addEventListener("input", (e) => {

    myData1.value = null

    document.getElementById("myHiTag").innerHTML = null

    const nameValue2 = e.target.value;
    if (nameValue2.length == 0) {
        getData3()
    }
    getData2(nameValue2)

})

getData3()