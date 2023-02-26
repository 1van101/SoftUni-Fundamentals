function findLargestNum(n1, n2, n3){
    let largestNum = n1;
    
    if (n2 > largestNum){
        largestNum = n2;
    }
    if (n3 > largestNum){
        largestNum = n3;
    }
    console.log(`The largest number is ${largestNum}.`);

}

findLargestNum(-3, -5, -22.5)