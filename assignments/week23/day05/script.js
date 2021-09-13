document.querySelector(".card-number-input").oninput = () => {
    let value = document.querySelector(".card-number-input").value;
    let res = "";
    for (let i = 0; i < value.length; i++) {
        if (i == 0 || i == 1 || i == 2 || i == 3 || i == 15 || i == 14 || i == 13 || i == 12) {
            res += value[i]
        } else {
            res += "*"
        }
    }
    document.querySelector(".card-number-box").innerText = res;
}

document.querySelector(".card-holder-input").oninput = () => {
    let value = document.querySelector(".card-holder-input").value;
    document.querySelector(".card-holder-name").innerText = value;
}

document.querySelector(".month-input").oninput = () => {
    let value = document.querySelector(".month-input").value;
    document.querySelector(".exp-month").innerText = value;
}

document.querySelector(".year-input").oninput = () => {
    let value = document.querySelector(".year-input").value;
    document.querySelector(".exp-year").innerText = value;
}

document.querySelector(".cvv-input").onmouseleave = () => {
    document.querySelector(".front").style.transform = "perspective(800px) rotateY(0deg)"
    document.querySelector(".back").style.transform = "perspective(800px) rotateY(180deg)"
}
document.querySelector(".cvv-input").onmouseenter = () => {
    document.querySelector(".front").style.transform = "perspective(800px) rotateY(-180deg)"
    document.querySelector(".back").style.transform = "perspective(800px) rotateY(0deg)"
}

document.querySelector(".cvv-input").oninput = () => {
    let value = document.querySelector(".cvv-input").value;
    document.querySelector(".cvv-box").innerText = value;
}

