// TODO:
function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/'
    let loadBtn = document.querySelector('legend')
    let addTaskBtn = document.getElementById('create-task-btn')
    let taskTitle = document.getElementById('title')
    let taskDescription = document.getElementById('description')
    let allContainers = Array.from(document.querySelectorAll('.task-list'))
    let toDoContainer = document.querySelector('#todo-section .task-list')
    let inContainer = document.querySelector('#in-progress-section .task-list')
    let codeContainer = document.querySelector('#code-review-section .task-list')
    let doneContainer = document.querySelector('#done-section .task-list')

    let allTasks = {
        'ToDo': toDoContainer,
        'In Progress': inContainer,
        'Code Review': codeContainer,
        'Done': doneContainer
    }
    let buttonsNames = {
        'ToDo': 'Move to In Progress',
        'In Progress': 'Move to Code Review',
        'Code Review': 'Move to Done',
        'Done': 'Close'
    }
    loadBtn.addEventListener('click', loadTasks)
    addTaskBtn.addEventListener('click', addTask)

    async function loadTasks(e) {
        e?.preventDefault()

        let response = await fetch(BASE_URL)
        let data = await response.json()
        clearContainers()
        for (const line of Object.values(data)) {

            let { title, description, status, _id } = line
            console.log(status)
            let newLi = createElement('li', allTasks[status], 'task')

            createElement('h3', newLi, null, title)
            createElement('p', newLi, null, description)
            let newBtn = createElement('button', newLi, null, buttonsNames[status])
            newBtn.addEventListener('click', moveTask)

            async function moveTask(e) {
                let parent = e.currentTarget.parentNode.parentNode.parentNode
                let newStatus = ''
                let newMethod = 'PATCH'

                if (parent.id === 'todo-section') {
                    newStatus = 'In Progress'

                } else if (parent.id === 'in-progress-section') {
                    newStatus = 'Code Review'
                } else if (parent.id === 'code-review-section') {
                    newStatus = 'Done'
                } else if (parent.id === 'done-section') {
                    newMethod = 'DELETE'
                }
                let body = {
                    title: title,
                    description: description,
                    status: newStatus
                }
                if (parent.id === 'done-section') {
                    await fetch(`${BASE_URL}${_id}`, {method: newMethod})
                } else {
                    let httpHeaders = { method: newMethod, body: JSON.stringify(body) }
                    await fetch(`${BASE_URL}${_id}`, httpHeaders)
                }
                let httpHeaders = { method: newMethod, body: JSON.stringify(body) }
                await fetch(`${BASE_URL}${_id}`, httpHeaders)
                loadTasks()
            }
        }
    }

    async function addTask(e) {
        e?.preventDefault()

        let title = taskTitle.value
        let description = taskDescription.value
        console.log(taskDescription.value)
        if (!title.trim() || !description.trim()) {
            return
        }

        let status = 'ToDo'
        let body = {
            title: title,
            description: description,
            status: status
        }
        console.log(body)
        let httpHeaders = { method: 'POST', body: JSON.stringify(body) }
        await fetch(BASE_URL, httpHeaders)
        taskTitle.value = ''
        taskDescription.value = ''
        loadTasks()
    }

    function createElement(element, parent, className, text) {
        let newEl = document.createElement(element)
        if (className) {
            newEl.classList = className
        }
        newEl.textContent = text
        parent.appendChild(newEl)
        return newEl
    }
    function clearContainers() {
        allContainers.forEach(element => {
            element.innerHTML = ''
        });
    }
}



attachEvents();