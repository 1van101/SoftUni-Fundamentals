function toyShop(input){
    let excursionPrice = Number(input[0]);

    toysPrices = {
        1: 2.60,            //puzzlePrice
        2: 3,               //dollPrice
        3: 4.10,            //bearPrice
        4: 8.20,            //minionPrice
        5: 2                //truckPrice
    };

    let totalToys = 0;
    let totalProfit = 0;
    let i = 1;
    while (input[i]){
        let numberToys = Number(input[i]);
        totalToys += numberToys;
        totalProfit += toysPrices[i] * numberToys;
        
        i++;
    }

    if (totalToys >= 50){
        totalProfit *= 0.75;
    }
    totalProfit *= 0.9

    if (totalProfit >= excursionPrice){
        console.log(`Yes! ${(totalProfit - excursionPrice).toFixed(2)} lv left.`);
    }else{
        console.log(`Not enough money! ${(excursionPrice - totalProfit).toFixed(2)} lv needed.`);
    }
}

toyShop(["320",
"8",
"2",
"5",
"5",
"1"])

