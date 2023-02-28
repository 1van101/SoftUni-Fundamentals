function solve(n1, n2, n3){
    let nums = [n1, n2, n3];
    let negatives = 0;

    nums.forEach(function(n){
        if(n < 0){
            negatives++;
        }
    })
    
    if(negatives % 2 != 0){
        console.log('Negative')
    }else{
        console.log('Positive')
    }
}
