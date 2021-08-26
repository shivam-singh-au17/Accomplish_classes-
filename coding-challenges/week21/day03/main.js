
let input = prompt("Enter Number");
let limit = prompt("Enter Limit");

function printTable(input = 10, limit = 10) {
    for (i = 1; i <= limit; i++) {
        console.log(`${input} * ${i} = ${input * i}`);
    }
}

if (input.length == 0 && limit.length == 0) {
    printTable()
} else {
    printTable(input, limit)
}