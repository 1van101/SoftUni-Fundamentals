function solve(ch1, ch2){
    let firstChar = ch1.charCodeAt();
    let secondChar = ch2.charCodeAt();
    let start;
    let end;
    let res = '';

    if (firstChar > secondChar){
        start = secondChar;
        end = firstChar;
    }else{
        start = firstChar;
        end = secondChar;
    }

    for(let i = start + 1; i < end; i++){
        res += String.fromCharCode(i) + ' ';
    }

    console.log(res.trim())
}
