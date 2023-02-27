function solve(year){
    let status = ''
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0){
        status = 'yes';
    }else{
        status = 'no';
    }
    console.log(status)
}


solve(1984)
