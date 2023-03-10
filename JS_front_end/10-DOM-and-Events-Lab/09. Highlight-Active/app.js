function focused() {
    let targets = document.querySelectorAll('div div input')
    
    for (const el of targets) {
        el.addEventListener('focus', (e) => {
            e.currentTarget.parentNode.classList.add('focused');
        });
        
        el.addEventListener('blur', (e) => {
            e.currentTarget.parentNode.classList.remove('focused');
        });

    }
}
