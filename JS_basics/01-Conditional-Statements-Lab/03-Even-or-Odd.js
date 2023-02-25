function evenOrOdd(input){
    let firstNum = Number(input[0]);
    let secondNum = Number(input[1]);
    let type = '';
    if (firstNum % 2 == 0){
        type = 'even';
    }else{
        type = 'odd';
    }
    console.log(type)
}

evenOrOdd(["2"])