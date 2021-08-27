

let input = prompt("Enter Any Number");

function armstrong(num) {

    let number = String(num)
    n = number.length
    let output = 0;

    for (let i = 0; i < number.length; i++) {
        output += Number(number[i]) ** n;
    }
    if (output == Number(number)) {
        alert('Armstrong Number')
    }
    else {
        alert('Not Armstrong Number')
    }

}

armstrong(input)