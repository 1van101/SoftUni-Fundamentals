function numbersInfo(input){
    let number = Number(input[0]);
    let numberInfo = ''
    if (number < 100){
        numberInfo = 'Less than 100';
    }else if (number <= 200){
        numberInfo = 'Between 100 and 200';
    }else{
        numberInfo = 'Greater than 200';
    }
    console.log(numberInfo)
}