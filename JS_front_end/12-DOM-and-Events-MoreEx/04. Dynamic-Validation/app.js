function validate() {
    let emailInput = document.getElementById('email');
    emailInput.addEventListener('change', emailValidation)


    function emailValidation() {
        const emailIsValid = /^[a-z]+@[a-z]+.[a-z]+$/.test(emailInput.value);  
        if (emailIsValid){
            emailInput.classList.remove('error');   
        }else{
            emailInput.classList.add('error');
        }
    }
}