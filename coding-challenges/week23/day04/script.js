

let monthsToPay = document.getElementById("MonthsToPay");
let monthlyPayment = document.getElementById("MonthlyPayment");

if (document.getElementById("MonthsToPay").value == "") {
    document.getElementById("MonthsToPay").value = "00.00";
}

monthsToPay.addEventListener("input", (e) => {

    let loanAmount = document.getElementById("LoanAmount").value;
    let interestRate = document.getElementById("InterestRate").value;

    let totalAmt = Number(loanAmount) + (Number(loanAmount) * Number(interestRate) / 100);
    let MonToPay = totalAmt / Number(e.target.value)
    monthlyPayment.textContent = Math.floor(MonToPay)

})