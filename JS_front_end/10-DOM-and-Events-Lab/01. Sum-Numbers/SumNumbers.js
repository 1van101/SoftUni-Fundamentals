function calc() {
    let firstNum = document.getElementById('num1').value;
    let secondNum = document.getElementById('num2').value;

    let res = Number(firstNum) + Number(secondNum);
    document.getElementById("sum").value = res;
}
