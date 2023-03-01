function solve(num){
    let matrix = [];
    
    for (let i = 0; i < num; i++){
        let currMatrix = [];
        for (let i = 0; i < num; i++){
            currMatrix.push(num);
        }
        matrix.push(currMatrix);
    }

    for (let i = 0; i < num; i++){
        console.log(...matrix[i]);
    }
    
}

solve(3)