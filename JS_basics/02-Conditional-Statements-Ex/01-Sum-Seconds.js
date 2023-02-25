function secondsSum(input){
    let firstTime = Number(input[0]);
    let secondTime = Number(input[1]);
    let thirdTime = Number(input[2]);

    let totalSeconds = firstTime + secondTime + thirdTime;
    let minutes = Math.floor(totalSeconds / 60);
    let seconds = totalSeconds % 60;

    console.log(`${minutes}:${('0' + seconds).slice(-2)}`);
}

secondsSum(["14", "12",
"10"])

