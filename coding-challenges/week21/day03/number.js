
let str = prompt("Enter Start Number");
let end = prompt("Enter End Number");

function printNumber(str = 1, end=100) {
    for (i = end; i >= str; i--) {
        console.log(i);
    }
}

if (str.length == 0 && end.length == 0) {
    printNumber()
} else {
    printNumber(str, end)
}