function lockedProfile() {
    let buttons = document.querySelectorAll('button');

    for (const bttn of buttons) {
        bttn.addEventListener('click', showMore)
    }

    function showMore(event){
        console.log(event.target.textContent)
        let button = event.target;
        let currentProfile = button.parentElement;
        let moreInfo = currentProfile.getElementsByTagName('div')[0];
        let status = currentProfile.querySelector('input[type="radio"]:checked').value;

        
        if (status === 'unlock') {
            if (button.textContent === 'Show more') {
                moreInfo.style.display = 'block';
                button.textContent = 'Hide it';
            } else if (button.textContent === 'Hide it') {
                moreInfo.style.display = 'none';
                button.textContent = 'Show more';
            }
        }
    }

    
}