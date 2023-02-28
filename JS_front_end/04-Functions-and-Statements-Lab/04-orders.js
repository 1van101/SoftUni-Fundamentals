function solve(product, qty){
    let productsPrices = {
        'coffee': 1.5,
        'water': 1,
        'coke': 1.4,
        'snacks': 2
    }

    return (productsPrices[product] * qty).toFixed(2);
}