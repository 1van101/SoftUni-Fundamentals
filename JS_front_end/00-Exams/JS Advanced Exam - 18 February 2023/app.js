window.addEventListener('load', solve);

function solve() {
    let mainContainer = document.getElementById('main');
    let bodyContainer = document.getElementById('body');
    let inputs = Array.from(document.querySelectorAll('input'));
    let fname = document.getElementById('first-name');
    let lname = document.getElementById('last-name');
    let peopleCount = document.getElementById('people-count');
    let date = document.getElementById('from-date');
    let daysCount = document.getElementById('days-count');
    let nextBtn = document.getElementById('next-btn');
    let previewContainer = document.querySelector('.ticket-info-container .first-container .ticket-info-list')
    let confirmContainer = document.querySelector('.confirm-container .first-container .confirm-ticket')

    let initialData = {}

    nextBtn.addEventListener('click', buyTicket)

    function buyTicket(e) {
        e.preventDefault();
        if (!fname.value.trim() || !lname.value.trim() || !peopleCount.value.trim() || !date.value.trim() || !daysCount.value.trim()) {
            return
        }

        initialData = {
            fname: fname.value,
            lname: lname.value,
            peopleCount: peopleCount.value,
            date: date.value,
            daysCount: daysCount.value
        }

        nextBtn.disabled = true;
        let newLi = document.createElement('li')
        let newArticle = document.createElement('article')
        let newH3 = document.createElement('h3')
        let newPDate = document.createElement('p')
        let newPDaysCount = document.createElement('p')
        let newPPeopleCount = document.createElement('p')
        let editBtn = document.createElement('button')
        let continueBtn = document.createElement('button')

        newLi.classList = 'ticket'
        editBtn.classList = 'edit-btn'
        continueBtn.classList = 'continue-btn'

        newH3.textContent = `Name: ${fname.value} ${lname.value}`
        newPDate.textContent = `From date: ${date.value}`
        newPDaysCount.textContent = `For ${daysCount.value} days`
        newPPeopleCount.textContent = `For ${peopleCount.value} people`
        editBtn.textContent = 'Edit'
        continueBtn.textContent = 'Continue'

        newArticle.appendChild(newH3)
        newArticle.appendChild(newPDate)
        newArticle.appendChild(newPDaysCount)
        newArticle.appendChild(newPPeopleCount)

        newLi.appendChild(newArticle)
        newLi.appendChild(editBtn)
        newLi.appendChild(continueBtn)

        previewContainer.appendChild(newLi)
        clearInput()

        editBtn.addEventListener('click', editInformation)
        continueBtn.addEventListener('click', () => continueReservation(newLi, editBtn, continueBtn))
    }

    function editInformation() {
        nextBtn.disabled = false;
        previewContainer.innerHTML = ''
        fname.value = initialData.fname;
        lname.value = initialData.lname;
        peopleCount.value = initialData.peopleCount;
        date.value = initialData.date;
        daysCount.value = initialData.daysCount;
    }

    function continueReservation(newLi, editBtn, continueBtn) {
        confirmContainer.appendChild(newLi)
        editBtn.remove()
        continueBtn.remove()

        let confirmBtn = document.createElement('button')
        let cancelBtn = document.createElement('button')

        confirmBtn.classList = 'confirm-btn'
        cancelBtn.classList = 'cancel-btn'
        newLi.classList = 'ticket-content'
        confirmBtn.textContent = 'Confirm'
        cancelBtn.textContent = 'Cancel'

        newLi.appendChild(confirmBtn)
        newLi.appendChild(cancelBtn)

        cancelBtn.addEventListener('click', () =>{
            confirmContainer.innerHTML = ''
            nextBtn.disabled = false;
        })
        confirmBtn.addEventListener('click', () =>{
            mainContainer.remove();
            let newH1 = document.createElement('h1');
            let backBtn = document.createElement('button');
            backBtn.textContent = 'Back';
            backBtn.id = 'back-btn'
            newH1.id = 'thank-you'
            newH1.textContent = 'Thank you, have a nice day! '
            bodyContainer.appendChild(newH1)
            bodyContainer.appendChild(backBtn)
            backBtn.addEventListener('click', function(){location.reload()});
        })
    }
    function clearInput() {
        inputs.forEach(el => el.value = '')
    }
}




