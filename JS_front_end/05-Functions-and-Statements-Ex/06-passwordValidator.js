function solve(psswrd) {
    function length(pass) {
        return (pass.length >= 6 && pass.length <= 10);
    }

    function typeOfChars(pass) {
        re = /^[A-Za-z0-9]+$/;
        return re.test(pass)
    }

    function atLeast2Digits(pass) {
        re = /[0-9]{2,}/;
        return re.test(pass)
    }

    if (length(psswrd) == true && typeOfChars(psswrd) == true && atLeast2Digits(psswrd) == true){
        console.log('Password is valid');
        return
    }
    
    if (length(psswrd) != true){
        console.log('Password must be between 6 and 10 characters');
    }
    if (typeOfChars(psswrd) != true){
        console.log('Password must consist only of letters and digits');
    }
    if (atLeast2Digits(psswrd) != true){
        console.log('Password must have at least 2 digits');
    }
    
}

solve('lll12')


