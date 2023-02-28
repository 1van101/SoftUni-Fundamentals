function solve(arr){
    arr.sort((x, y) => x.localeCompare(y));
    
    for (let i = 1; i <= arr.length; i++){
        console.log(`${i}.${arr[i - 1]}`)
    }
}

solve(["john", "boab",'Bobb', "christina", "ema", 'Zegna'])