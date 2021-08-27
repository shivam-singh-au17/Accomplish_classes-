

let input = prompt("Enter Your Number");

if (input <= 1 || input.length == 0) {
    alert("Not Prime")
} else {
    let count = 0;
    for (let i = 2; i <= input; i++) {
        if (input % i == 0) {
            count++;
        }
    }
    if (count == 1) {
        alert("Prime Number")
    } else {
        alert("Not Prime")
    }
}