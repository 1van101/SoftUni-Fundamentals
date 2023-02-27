function solve(startIndex, endIndex){
    let res = ''
    let count = 0
    
    for(let i = startIndex; i <= endIndex; i++){
        res += i + " ";
        count += i
    }

    console.log(`${res}\nSum: ${count}`)
}