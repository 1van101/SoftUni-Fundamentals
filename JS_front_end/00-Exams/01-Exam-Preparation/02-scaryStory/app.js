window.addEventListener("load", solve);

function solve() {
  let inputs = Array.from(document.querySelectorAll('input')).slice(0, 4);
  let fName = document.getElementById('first-name');
  let lName = document.getElementById('last-name');
  let age = document.getElementById('age');
  let storyTitle = document.getElementById('story-title');
  let genre = document.getElementById('genre');
  let story = document.getElementById('story');
  let publishButton = document.getElementById('form-btn');
  let previewList = document.getElementById('preview-list');
  let main = document.getElementById('main');


  publishButton.addEventListener('click', publishStory);

  function publishStory() {
    let allDataInputs = {
      firstName: fName.value,
      lastName: lName.value,
      age: age.value,
      storyTitle: storyTitle.value,
      story: story.value
    }

    if (validInput()) {
      publishButton.disabled = true;

      const newLi = document.createElement('li');
      newLi.classList = 'story-info'

      const newArticle = document.createElement('article');

      const saveButton = document.createElement('button');
      saveButton.classList = 'save-btn';
      saveButton.textContent = 'Save Story';

      const editButton = document.createElement('button');
      editButton.classList = 'edit-btn';
      editButton.textContent = 'Edit Story';

      const deleteButton = document.createElement('button');
      deleteButton.classList = 'delete-btn';
      deleteButton.textContent = 'Delete Story';

      newArticle.innerHTML += `<h4>Name: ${fName.value} ${lName.value}</h4>`
        + `<p>Age: ${age.value}</p>`
        + `<p>Title: ${storyTitle.value}</p>`
        + `<p>Genre: ${genre.value}</p>`
        + `<p>${story.value}</p>`;

      newLi.appendChild(newArticle);
      newLi.appendChild(saveButton);
      newLi.appendChild(editButton);
      newLi.appendChild(deleteButton);

      previewList.appendChild(newLi)

      editButton.addEventListener('click', editStory);
      saveButton.addEventListener('click', saveStory);
      deleteButton.addEventListener('click', deleteStory);

      function editStory() {
        fName.value = allDataInputs.firstName;
        lName.value = allDataInputs.lastName;
        age.value = allDataInputs.age;
        storyTitle.value = allDataInputs.storyTitle;
        story.value = allDataInputs.story;
        
        deleteButton.disabled = true
        editButton.disabled = true
        saveButton.disabled = true
        publishButton.disabled = false
        previewList.removeChild(newLi)
      }

      function saveStory() {
        main.innerHTML = ''
        let newH1 = document.createElement('h1')
        newH1.textContent = 'Your scary story is saved!'
        newH1.setAttribute('id', 'main')
        main.appendChild(newH1)

      }

      function deleteStory() {
        previewList.removeChild(newLi)
        publishButton.disabled = false
      }

      fName.value = '';
      lName.value = '';
      age.value = '';
      storyTitle.value = '';
      story.value = '';
    }
  }



  function validInput() {
    for (const el of inputs) {

      if (el.value.trim() === '') {
        return false
      }

    }
    if (story.value.trim() !== '') {
      return true
    }
  }
}