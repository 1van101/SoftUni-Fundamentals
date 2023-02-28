function solve(n1, n2, operation){
    let calculatorOperations = {
        'multiply': (x, y) => x * y,
        'divide': (x, y) => x / y,
        'add': (x, y) => x + y,
        'subtract': (x, y) => x - y,
    }

    return calculatorOperations[operation](n1, n2);
}