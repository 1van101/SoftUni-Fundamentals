function solve(arr){
    let sumEvens = 0;
    let sumOdds = 0;

    for (i = 0; i < arr.length; i++){
        if (arr[i] % 2 == 0){
            sumEvens += arr[i];
        }else{
            sumOdds += arr[i];
        }
    }
    console.log(sumEvens - sumOdds)
}

solve([1, 2, 3, 4])