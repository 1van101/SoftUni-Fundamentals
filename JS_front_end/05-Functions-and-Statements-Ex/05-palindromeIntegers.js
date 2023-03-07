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

// =======================================================================================
// function solve(input) {
//     let isPalindrome = (num) => Number([...String(num)].reverse().join('')) === num;

//     input
//         .forEach((element) => {
//             console.log(isPalindrome(element))
//         });
// }

// ===========================================================================================
// function solve(input) {
//     let isPalindrome = (num) => Number([...String(num)].reverse().join('')) === num;

//     return input
//         .map(isPalindrome)
//         .join('\n');
// }
solve([32, 2, 232, 1010])