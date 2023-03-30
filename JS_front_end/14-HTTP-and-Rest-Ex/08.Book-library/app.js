function attachEvents() {
    let buttons = document.getElementsByTagName('button')
    let loadButton = buttons[0];
    let submitBtn = buttons[buttons.length - 1];
    let [titleInput, authorInput] = document.getElementsByTagName('input');
    let formName = document.getElementsByTagName('h3')[0]
    let bodyContainer = document.getElementsByTagName('tbody')[0];
    const BASE_URL = 'http://localhost:3030/jsonstore/collections/books'
    let allBooks = {}
    let bookKey = '';
    
    loadButton.addEventListener('click', loadBooks)
    submitBtn.addEventListener('click', submitBook)
    
    async function loadBooks() {
        bodyContainer.innerHTML = ''
        let response = await fetch(BASE_URL)
        let data = await response.json()
        allBooks = data
        for (const [key, book] of Object.entries(data)) {
            let { author, title } = book
            let newRow = document.createElement('tr')

            let titleCol = document.createElement('td')
            titleCol.textContent = title

            let authorCol = document.createElement('td')
            authorCol.textContent = author

            let btnsCol = document.createElement('td')

            let editBtn = document.createElement('button')
            editBtn.id = key
            editBtn.textContent = 'Edit'

            let delBtn = document.createElement('button')
            delBtn.id = key
            delBtn.textContent = 'Delete'

            btnsCol.appendChild(editBtn)
            btnsCol.appendChild(delBtn)

            newRow.appendChild(titleCol)
            newRow.appendChild(authorCol)
            newRow.appendChild(btnsCol)

            bodyContainer.appendChild(newRow)
            delBtn.addEventListener('click', delBook)
            editBtn.addEventListener('click', editBook)
        }
    }

    async function submitBook() {
        let title = titleInput.value;
        let author = authorInput.value;
        if (title.trim() === '' || author.trim() === '') {
            return
        }
        let httpHeaders = {
            method: 'POST',
            body: JSON.stringify({ title, author })
        }
        fetch(BASE_URL, httpHeaders)
        titleInput.value = ''
        authorInput.value = ''
        loadBooks()
    }

    async function editBook() {
        submitBtn.removeEventListener('click', submitBook)
        submitBtn.addEventListener('click', saveUpdatedBook)
        bookKey = this.id
        formName.textContent = 'Edit FORM';
        submitBtn.textContent = 'Save';
        titleInput.value = allBooks[bookKey].title;
        authorInput.value = allBooks[bookKey].author;
    }

    async function delBook() {
        const bookId = this.id
        let url = `${BASE_URL}/${bookId}`
        fetch(url, { method: 'DELETE' })
        loadBooks()
    }

    async function saveUpdatedBook(){
        if (titleInput.value.trim() === '' || authorInput.value.trim() === ''){
            return
        }
        let url = `${BASE_URL}/${bookKey}`
        let body = {
            title: titleInput.value,
            author: authorInput.value
        }
        let options = {
            method: "PUT",
            body: JSON.stringify(body)
        }

        fetch(url, options)
        
        formName.textContent = 'FORM'
        submitBtn.textContent = 'Submit'
        titleInput.value = '';
        authorInput.value = '';
        loadBooks()
        
        submitBtn.removeEventListener('click', saveUpdatedBook)
        submitBtn.addEventListener('click', submitBook)
    }
}

attachEvents();