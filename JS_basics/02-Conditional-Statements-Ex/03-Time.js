function time(input){
    let hours = Number(input[0]);
    let minutes = Number(input[1]);
    let newTotalTime = (hours * 60) + minutes + 15;

    let newHours = Math.floor(newTotalTime / 60) % 24;
    let newMinutes = newTotalTime % 60;

    console.log(`${newHours}:${('0' + newMinutes).slice(-2)}`);
}

time(["12", "49"])





