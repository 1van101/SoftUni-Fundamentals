function solve(n1, n2, n3){
    let minNum = n1;
    for(let n of [n2, n3]){
        if (n < minNum){
            minNum = n;
        }
    }
    console.log(minNum)
}