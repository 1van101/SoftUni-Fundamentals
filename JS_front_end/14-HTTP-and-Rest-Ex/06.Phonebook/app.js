function attachEvents() {
    let phonebookContainer = document.getElementById('phonebook');
    let loadPhonebookButton = document.getElementById('btnLoad');
    let createEntryButton = document.getElementById('btnCreate');
    let personInput = document.getElementById('person');
    let phoneInput = document.getElementById('phone');
    
    const BASE_URL = 'http://localhost:3030/jsonstore/phonebook';

    loadPhonebookButton.addEventListener('click', loadContacts)
    async function loadContacts() {

        phonebookContainer.innerHTML = ''
        let response = await fetch(BASE_URL);
        let data = await response.json();
        for (const value of Object.values(data)) {
            let { person, phone, _id } = value
            let newLi = document.createElement('li');
            let deleteButton = document.createElement('button');

            deleteButton.textContent = 'Delete';
            newLi.textContent = `${person}: ${phone}`;
            newLi.appendChild(deleteButton);
            phonebookContainer.appendChild(newLi);
            
            deleteButton.addEventListener('click', () => {
                fetch(`${BASE_URL}/${value._id}`, {
                    method: 'DELETE'
                });
                
                phonebookContainer.removeChild(newLi);
            })
        }
    }

    createEntryButton.addEventListener('click', () => {
        const person = personInput.value.trim()
        const phone = phoneInput.value.trim()
        
        fetch(BASE_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                person,
                phone
            })
        });
        personInput.value = ''
        phoneInput.value = ''
        loadContacts
    })



}

attachEvents();