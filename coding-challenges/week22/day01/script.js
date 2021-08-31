

let myBtn = document.getElementById("Submit");

myBtn.addEventListener("click", (e) => {

    e.preventDefault();

    let myRes = document.getElementById("result");
    let num1 = document.getElementById("number01").value;
    let num2 = document.getElementById("number02").value;
    
    if (num1.length > 0 && num2.length > 0) {

        let sum = Number(num1) + Number(num2);
        console.log('sum:', sum)
        myRes.innerHTML = sum;
        myRes.style.background = "green"
        
        document.getElementById("number01").value = null;
        document.getElementById("number02").value = null;
        
    } else {
        myRes.innerHTML = "Enter Your Number";
        myRes.style.background = "red"
    }

})