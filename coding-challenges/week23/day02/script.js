
function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}

let robot = document.getElementById("Robot");
let Result = document.getElementById("result");
let rock = document.getElementById("Rock");
let paper = document.getElementById("Paper");
let scissor = document.getElementById("Scissor");

function printResult(ans) {
    if (ans == 1) {
        robot.innerHTML = "Rock"
    } else if (ans == 2) {
        robot.innerHTML = "Paper"
    } else {
        robot.innerHTML = "Scissor"
    }
}


function printAllResult(ans, value) {
    if ((ans == 1 && value == 1) || (ans == 2 && value == 2) || (ans == 3 && value == 3)) {
        Result.innerHTML = "Koi Nahi Jita";
        Result.style.color = "red"
    } else if (ans == 1 && value == 2) {
        Result.innerHTML = "Apana Paper Bhai Jita"
        Result.style.color = "green"
    } else if (ans == 1 && value == 3) {
        Result.innerHTML = "Apana Rock Bhai Jita"
        Result.style.color = "blue"
    } else if (ans == 2 && value == 3) {
        Result.innerHTML = "Apana Scissor Bhai Jita"
        Result.style.color = "orange"
    } else {
        Result.innerHTML = "Apana Scissor Bhai Jita"
        Result.style.color = "orange"
    }
}

let rockBtn = document.getElementById("Rock").value;
rock.addEventListener("click", () => {

    let ans = Math.floor(getRandomArbitrary(1, 4))
    printResult(ans)
    printAllResult(ans, rockBtn)

})

paper.addEventListener("click", () => {

    let paperBtn = document.getElementById("Paper").value;
    let ans = Math.floor(getRandomArbitrary(1, 4))
    printResult(ans)
    printAllResult(ans, paperBtn)

})

scissor.addEventListener("click", () => {

    let scissorBtn = document.getElementById("Scissor").value;
    let ans = Math.floor(getRandomArbitrary(1, 4))
    printResult(ans)
    printAllResult(ans, scissorBtn)

})

