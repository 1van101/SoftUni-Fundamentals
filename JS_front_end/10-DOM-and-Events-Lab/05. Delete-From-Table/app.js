function deleteByEmail() {
    let input = document.querySelector('input[name="email"]').value;
    let emails = document.querySelectorAll("#customers tr td:nth-child(even)");
    let isDeleted = false;
    
    for (let email of emails) {
        if (email.textContent === input) {
            email.parentNode.remove();
            isDeleted = true;
        }
    }

    document.getElementById("result").textContent = isDeleted ? 'Deleted.' : 'Not found.'

}


