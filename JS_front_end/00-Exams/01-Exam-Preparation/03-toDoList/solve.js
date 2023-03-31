function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/'

    let inputField = document.getElementById('title');
    let addBtn = document.getElementById('add-button');
    let loadBtn = document.getElementById('load-button');
    let tasksContainer = document.getElementById('todo-list');

    loadBtn.addEventListener('click', loadTasks)
    addBtn.addEventListener('click', addTask)

    async function loadTasks(event) {
        tasksContainer.innerHTML = ''
        event?.preventDefault();
        try {
            let response = await fetch(BASE_URL);
            let data = await response.json();

            for (const task of Object.values(data)) {
                let { name, _id } = task

                let newLi = document.createElement('li');
                let newSpan = document.createElement('span');
                let removeBtn = document.createElement('button');
                let editBtn = document.createElement('button');

                newSpan.textContent = name;
                removeBtn.textContent = 'Remove';
                editBtn.textContent = 'Edit';

                newLi.append(newSpan, removeBtn, editBtn);
                tasksContainer.appendChild(newLi);

                removeBtn.addEventListener('click', function () { deleteTask(_id) })
                editBtn.addEventListener('click', function (event) { editTask(event, _id) })
            }
        } catch (err) {
            console.error(err);
        }
    }

    async function addTask(event) {
        event?.preventDefault();
        let name = inputField.value;

        if (!name) {
            return
        };

        let httpHeaders = {
            method: 'POST',
            body: JSON.stringify({ name })
        }
        await fetch(BASE_URL, httpHeaders)
        inputField.value = ''
        loadTasks()
    }

    async function deleteTask(id) {
        let url = `${BASE_URL}${id}`
        await fetch(url, { method: 'DELETE' })
        loadTasks()
    }

    async function editTask(event, id) {
        let parent = event.target.parentNode
        let [span, _removeBtn, editBtn] = Array.from(parent.children)

        let newInput = document.createElement('input');
        newInput.value = span.textContent

        let submitBtn = document.createElement('button');
        submitBtn.textContent = 'Submit'

        parent.prepend(newInput);
        parent.appendChild(submitBtn)
        span.remove()
        editBtn.remove()

        submitBtn.addEventListener('click', async () => {
            if (!newInput.value) {
                return
            }
            const httpHeaders = {
                method: 'PATCH',
                body: JSON.stringify({ name: newInput.value })
            }
            try {
                await fetch(`${BASE_URL}${id}`, httpHeaders)
                loadTasks()
            } catch (error) {
                console.error(error)
            }
        });
    }
}

attachEvents();
