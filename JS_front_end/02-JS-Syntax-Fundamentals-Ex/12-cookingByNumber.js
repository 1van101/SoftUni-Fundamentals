function solve(num, com1, com2, com3, com4, com5) {
    let numToInt = Number(num);
    
    let operations = {
        'chop': x => x / 2,
        'dice': x => Math.sqrt(x),
        'spice': x => x + 1,
        'bake': x => x * 3,
        'fillet': x => x * 0.8
    };

    let arr = [com1, com2, com3, com4, com5];
    
    for (let i = 0; i < arr.length; i++){
        numToInt = operations[arr[i]](numToInt);
        console.log(numToInt);
    }
}


