window.addEventListener('load', solve);

function solve() {
    let inputs = Array.from(document.querySelectorAll('input'));
    let [genre, name, author, date] = inputs;
    let addBtn = document.getElementById('add-btn');
    let songsCollectionContainer = document.querySelector('.all-hits-container');
    let likesSectionParagraph = document.querySelector('.likes p');
    let savedSongsContainer = document.querySelector('.saved-container');
    let totalLikes = 0

    addBtn.addEventListener('click', addCollection)


    function clearInputFields() {
        inputs.forEach((el) => el.value = '')
    }

    function addCollection(event) {
        event.preventDefault()
        if (!genre.value.trim() || !name.value.trim() || !author.value.trim() || !date.value.trim()) {
            return
        }

        let divHitsInfo = document.createElement('div');
        divHitsInfo.classList = 'hits-info';

        let image = document.createElement('img');
        image.src = './static/img/img.png'

        let genreH2 = document.createElement('h2');
        genreH2.textContent = `Genre: ${genre.value}`

        let nameH2 = document.createElement('h2');
        nameH2.textContent = `Name: ${name.value}`

        let authorH2 = document.createElement('h2');
        authorH2.textContent = `Author: ${author.value}`

        let dateH2 = document.createElement('h3');
        dateH2.textContent = `Date: ${date.value}`

        let saveBtn = document.createElement('button');
        saveBtn.classList = 'save-btn';
        saveBtn.textContent = 'Save song'

        let likeBtn = document.createElement('button');
        likeBtn.classList = 'like-btn';
        likeBtn.textContent = 'Like song'

        let delBtn = document.createElement('button');
        delBtn.classList = 'delete-btn';
        delBtn.textContent = 'Delete'

        divHitsInfo.appendChild(image);
        divHitsInfo.appendChild(genreH2);
        divHitsInfo.appendChild(nameH2);
        divHitsInfo.appendChild(authorH2);
        divHitsInfo.appendChild(dateH2);
        divHitsInfo.appendChild(saveBtn);
        divHitsInfo.appendChild(likeBtn)
        divHitsInfo.appendChild(delBtn)
        
        songsCollectionContainer.appendChild(divHitsInfo);
        
        clearInputFields()

        likeBtn.addEventListener('click', (event) => {
            event.preventDefault();
            totalLikes++
            likesSectionParagraph.textContent = `Total Likes: ${totalLikes}`
            likeBtn.disabled = true
        })

        saveBtn.addEventListener('click', (event) => {
            event.preventDefault()
            divHitsInfo.remove()
            saveBtn.remove()
            likeBtn.remove()
            savedSongsContainer.appendChild(divHitsInfo)
        })

        delBtn.addEventListener('click', (event) => {
            event.preventDefault()
            delBtn.parentElement.remove()
        })
    }
}