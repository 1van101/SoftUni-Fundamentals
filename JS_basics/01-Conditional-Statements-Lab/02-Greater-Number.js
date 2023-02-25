function greaterNumber(input){
    let firstNum = Number(input[0]);
    let secondNum = Number(input[1]);
    let biggerNum = 0;

    if (firstNum > secondNum){
        biggerNum = firstNum;
    }else{
        biggerNum = secondNum
    }
    console.log(biggerNum)
}

greaterNumber(["5", "3"])