function sumDigits(num){
    let res = 0
    let numToStr = String(num);
    
    for (let i in numToStr){
        res += Number(numToStr[i]);
    }
    
    console.log(res);
}

sumDigits(32);