function solve(num){
    if (num === 100){
        return '100% Complete!'
    }

    let progressNum = num / 10;
    let bar = Array(10).fill('.');

    for (let i = 0; i < progressNum; i++){
        bar[i] = '%';
    }
    return `${num}% [${bar.join('')}]\nStill loading...`
}
