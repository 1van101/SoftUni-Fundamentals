function toggle() {
    let button = Array.from(document.getElementsByClassName('button'))[0];
    let divExtra = document.getElementById('extra');

    if (button.textContent === 'More'){
        divExtra.style.display = 'block';
        button.textContent = 'Less';
    }else{
        divExtra.style.display = 'none';
        button.textContent = 'More';
    }
}