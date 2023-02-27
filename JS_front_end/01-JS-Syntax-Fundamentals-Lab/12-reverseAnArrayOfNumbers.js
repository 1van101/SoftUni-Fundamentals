function solve(num, arr){
    let newArr = [];
    for(i = 0; i < num; i++){
        newArr.push(arr[i]);
    }
    console.log(newArr.reverse().join(' '))
}

