function solve(num){
    let sumEvens = 0;
    let sumOdds = 0;
    
    for (let current of String(num)){
        let currNum = Number(current)
        
        if (currNum % 2 == 0){
            sumEvens += currNum;
        }else{
            sumOdds += currNum;
        }
    }
    
    console.log(`Odd sum = ${sumOdds}, Even sum = ${sumEvens}`);
}

solve(10000435)