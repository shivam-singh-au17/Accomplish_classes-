
function chack01() {
    let checkbox = document.getElementById("UppercaseBox").checked;
    if (checkbox == true) {
        return true;
    } else {
        return false;
    }
}

function chack02() {
    let checkbox = document.getElementById("LowercaseBox").checked;
    if (checkbox == true) {
        return true;
    } else {
        return false;
    }
}

function chack03() {
    let checkbox = document.getElementById("NumbersBox").checked;
    if (checkbox == true) {
        return true;
    } else {
        return false;
    }
}

function chack04() {
    let checkbox = document.getElementById("SymbolsBox").checked;
    if (checkbox == true) {
        return true;
    } else {
        return false;
    }
}
let resultBox = document.getElementById("resultBox");
let myBtn = document.getElementById("submitBtn");

myBtn.addEventListener("click", () => {

    let len = document.getElementById("myValue").value;
    let cheBox1 = chack01();
    let cheBox2 = chack02();
    let cheBox3 = chack03();
    let cheBox4 = chack04();


    function printValue(temp) {
        let pass = '';
        for (i = 1; i <= Number(len); i++) {
            let char = Math.floor(Math.random() * temp.length + 1);
            pass += temp.charAt(char)
        }
        return pass;
    }

    function generateP() {

        let data01 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        let data02 = "abcdefghijklmnopqrstuvwxyz";
        let data03 = "0123456789";
        let data04 = "@#$%&^?/!";

        let case01 = data01 + data02 + data03 + data04;
        let case02 = data01 + data02 + data03;
        let case03 = data01 + data02;

        let case04 = data02 + data03 + data04;
        let case05 = data03 + data04;

        let case06 = data01 + data04;
        let case07 = data02 + data03;

        let case08 = data01 + data03;
        let case09 = data02 + data04;

        if (len < 4) {
            alert("Size must be 4 or above")
        } else if (cheBox1 == true && cheBox2 == true && cheBox3 == true && cheBox4 == true) {
            return printValue(case01)
        } else if (cheBox1 == true && cheBox2 == true && cheBox3 == true) {
            return printValue(case02)
        } else if (cheBox2 == true && cheBox3 == true && cheBox4 == true) {
            return printValue(case04)
        } else if (cheBox1 == true && cheBox2 == true) {
            return printValue(case03)
        } else if (cheBox3 == true && cheBox4 == true) {
            return printValue(case05)
        } else if (cheBox1 == true && cheBox4 == true) {
            return printValue(case06)
        } else if (cheBox2 == true && cheBox3 == true) {
            return printValue(case07)
        } else if (cheBox1 == true && cheBox3 == true) {
            return printValue(case08)
        } else if (cheBox2 == true && cheBox4 == true) {
            return printValue(case09)
        } else if (cheBox1 == true) {
            return printValue(data01)
        } else if (cheBox2 == true) {
            return printValue(data02)
        } else if (cheBox3 == true) {
            return printValue(data03)
        } else if (cheBox4 == true) {
            return printValue(data04)
        } else {
            alert("Enter Password Length And Your Letter Formate")
        }

    }

    resultBox.innerHTML = generateP();

})

