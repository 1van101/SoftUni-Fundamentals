function solve(fruit, weightGrams, pricePerKg){
    let weightKg = weightGrams / 1000
    let totalPrice = weightKg * pricePerKg;

    console.log(`I need $${totalPrice.toFixed(2)} to buy ${weightKg.toFixed(2)} kilograms ${fruit}.`)
}