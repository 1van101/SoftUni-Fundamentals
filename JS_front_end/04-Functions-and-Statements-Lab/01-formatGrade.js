function solve(num){
    let condition = '';
    if (num < 3){
        condition = `Fail (2)`;
    }else if (num < 3.5){
        condition = `Poor (${num.toFixed(2)})`;
    }else if (num < 4.5){
        condition = `Good (${num.toFixed(2)})`;
    }else if (num < 5.5){
        condition = `Very good (${num.toFixed(2)})`;
    }else{
        condition = `Excellent (${num.toFixed(2)})`;
    }

    console.log(condition)
}