function solve(n1, n2){
    function factorial(n){
        if (n === 0){
            return 1;
        }
        return n * factorial(n - 1);
    }

    let firstNumFactorial = factorial(n1);
    let secondNumFactorial = factorial(n2);

    return (firstNumFactorial / secondNumFactorial).toFixed(2);
}
