function runProgram(input) {

    var newInput = input.split("");
    
    var n = newInput.length;
    var result = "";
    var count = 1;
    var temp = newInput[0];
    for (var i = 1; i < n; i++) {
        if (newInput[i] == temp) {
            count++
        } else {
            if (count % 2 != 0) {
                result += temp;
                count = 1;
                temp = newInput[i];
            } else {
                result += "";
                count = 1;
                temp = newInput[i];
            }
        }
    }
    if (count % 2 != 0) {
        result += temp;
    } else {
        result += "";
    }
    if (result == "") {
        console.log("Empty String");
    } else {
        console.log(result);
    }
}

