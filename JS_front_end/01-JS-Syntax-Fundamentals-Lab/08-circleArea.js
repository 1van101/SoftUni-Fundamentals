function calculateCircleArea(arg){
    let result = ''
    
    switch(typeof arg){
        case 'number': result = (Math.PI * arg ** 2).toFixed(2); break;
        default: result = `We can not calculate the circle area, because we receive a ${typeof arg}.`; break;   
    }

    console.log(result);
}
