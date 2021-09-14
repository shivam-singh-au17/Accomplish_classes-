

let inputWarning = document.getElementById("warning")
let inputCount = document.getElementById("myHamming")

let inputBtn = document.getElementById("MyBtn");

function setWarning() {
    let p = document.createElement("p");
    p.innerText = "Please enter two string of equal length separated by a comma";
    p.style.color = "red"
    inputWarning.append(p);
}

inputBtn.addEventListener("click", () => {

    let inputValue = document.getElementById("MyTwoValue").value;

    let userInput = inputValue.toLowerCase()

    let temp = false;
    for (let i = 0; i < userInput.length; i++) {
        if (userInput.split(",").length == 2) {
            temp = true;
        }
    }

    let mystr = userInput.split(",");
    let str1 = mystr[0];
    let str2 = mystr[1];

    if (temp == true && str1.length == str2.length) {
        let i = 0;
        let count = 0;
        while (i < str1.length) {
            if (str1[i] != str2[i])
                count++;
            i++;
        }
        inputCount.innerText = count;
        inputWarning.innerHTML = null
    } else {
        setWarning()
    }

    document.getElementById("MyTwoValue").value = null

})


document.getElementById("MyTwoValue").addEventListener("click", () => {
    inputCount.innerHTML = "Result";
})
