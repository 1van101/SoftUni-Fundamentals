function cinemaIncome(input){
    let type = input[0];
    let rows = Number(input[1]);
    let cols = Number(input[2]);
    let totalCapacity = rows * cols;
    let income = 0;

    switch (type){
        case 'Premiere': income = totalCapacity * 12.00; break;
        case 'Normal': income = totalCapacity * 7.50; break;
        case 'Discount': income = totalCapacity * 5.00; break;
    }

    console.log(`${income.toFixed(2)} leva`)
}

cinemaIncome(["Premiere",
"10",
"12"])
