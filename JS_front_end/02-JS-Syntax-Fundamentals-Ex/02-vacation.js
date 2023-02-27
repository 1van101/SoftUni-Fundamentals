function solve(numberPeople, typeGroup, dayOfWeek) {
    
    function countPrice(day, people, price1, price2, price3) {
        switch (day) {
            case 'Friday': return price1 * people;
            case 'Saturday': return price2 * people;
            case 'Sunday': return price3 * people;
        }
    }

    let price = 0;

    switch (typeGroup) {
        case 'Students': price = countPrice(dayOfWeek, numberPeople, 8.45, 9.80, 10.46);
            if (numberPeople >= 30) {
                price *= 0.85;
            }
            break;
        case 'Business': price = countPrice(dayOfWeek, numberPeople, 10.90, 15.60, 16);
            if (numberPeople >= 100) {
                let priceForOne = price / numberPeople
                price -= priceForOne * 10;
            }
            break;
        case 'Regular': price = countPrice(dayOfWeek, numberPeople, 15, 20, 22.5);
            if (numberPeople >= 10 && numberPeople <= 20) {
                price *= 0.95;
            }
            break;
    }
    console.log(`Total price: ${price.toFixed(2)}`)
}
