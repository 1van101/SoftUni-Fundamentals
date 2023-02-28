function solve(arr){
    arr.sort(function(a, b){return a-b})
    let newArr = [];

    while (arr.length > 0){
        if (arr.length === 1){
            newArr.push(arr.pop());
            break;
        }
        newArr.push(arr.shift());
        newArr.push(arr.pop())
    }
    
    return newArr
    }
