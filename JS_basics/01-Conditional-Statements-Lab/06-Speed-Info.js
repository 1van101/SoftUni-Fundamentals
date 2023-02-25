function speedInformation(input){
    let speed = Number(input[0]);
    let speedString = '';

    if (speed <= 10){
        speedString = 'slow';
    }else if (speed <= 50){
        speedString = 'average';
    }else if (speed <= 150){
        speedString = 'fast';
    }else if (speed <= 1000){
        speedString = 'ultra fast';
    }else{
        speedString = 'extremely fast';
    }
    console.log(speedString);
}