function solve(input){
    for(let currWord of input){
        let currWordAsString = String(currWord);
        let palindromeFlag = true;

        for(let i = 0; i < Math.floor(currWordAsString.length / 2); i++){
            let lastIndex = currWordAsString.length - 1;

            if(currWordAsString[i] === currWordAsString[lastIndex - i]){
                continue
            }else{
                palindromeFlag = false;
                break;
            }
        }

        console.log(palindromeFlag);
    }
}

solve([32,2,232,1010])