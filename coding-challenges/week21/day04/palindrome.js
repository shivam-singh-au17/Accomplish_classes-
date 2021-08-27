

let input = prompt("Enter Any String Value");

let res = "";
for (let i = input.length - 1; i >= 0; i--) {
    res += input[i];
}
if (input.length == 0) {
    alert("Plase Enter Any String Value")
} else if (input.toUpperCase() == res.toUpperCase()) {
    alert("Palindrome")
} else {
    alert("Not Palindrome")
}