
function palindrome(data) {
    var result = true;
    for (var i = 0; i < data.length; i++) {
        if (data[i] != data[data.length - 1 - i]) {
            result = false;
            break;
        }
    }
    return result;
}


function runProgram(input) {
    
    var subStrLength = 0;
    for (var i = 0; i < input.length; i++) {
        var substr = "";
        for (var j = i; j < input.length; j++) {
            substr += input[j]
            var result = palindrome(substr);
            if (result == true) {
                if (substr.length > subStrLength) {
                    subStrLength = substr.length
                }
            }
        }
    }
    return subStrLength;
}

var str = "thisracecarisgood";
var result = runProgram(str);
console.log(result);

