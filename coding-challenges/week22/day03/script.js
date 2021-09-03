
let pushBtn = document.getElementById("PUSH_shivam");
let popBtn = document.getElementById("POP_singh");
let myStack = document.getElementById("shivamQueue");
let counter = 0;

pushBtn.addEventListener("click", () => {

    let myValue = document.getElementById("shivamsingh").value;

    if (myValue.length != 0) {

        if (myStack.innerText == "Stack Empty") {
            myStack.innerText = myValue
        } else
        
        if (counter == 0) {
            myStack.innerText = myValue
            } else {
                myStack.innerText += "," + myValue;
            }
            
    }


    counter++;
    document.getElementById("shivamsingh").value = null

})

popBtn.addEventListener("click", () => {

    let stack_my = document.getElementById("shivamQueue");

    let res = stack_my.innerText
    let resSplit = res.split(",")

    resSplit.shift()

    if (resSplit.length != 0) {
        stack_my.innerText = resSplit.join(",");
    } else {
        stack_my.innerText = "Empty Queue";
    }

});