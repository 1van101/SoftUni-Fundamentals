function solve(num1, num2, num3){
    function sum(n1, n2){
        return n1 + n2;
    }

    let res = sum(num1, num2);

    function subtract(res, n3){
        return res - n3;
    }

    console.log(subtract(res, num3));
}