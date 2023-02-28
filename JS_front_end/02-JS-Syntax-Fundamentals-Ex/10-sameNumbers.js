function solve(num){
    let arr = Array.from(String(num), Number);
    let result = arr.reduce((a, b) => a + b, 0);
    
    console.log(arr.every(x => x === arr[0]));
    console.log(result)
}

solve(2222222)