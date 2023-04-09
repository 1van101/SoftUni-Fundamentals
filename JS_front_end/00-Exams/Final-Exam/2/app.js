window.addEventListener('load', solve);

function solve() {
    let title = document.getElementById('title')
    let description = document.getElementById('description')
    let label = document.getElementById('label')
    let estimationPoints = document.getElementById('points')
    let assignee = document.getElementById('assignee')
    let createBtn = document.getElementById('create-task-btn')
    let deleteBtn = document.getElementById('delete-task-btn')
    let container = document.getElementById('tasks-section')
    let hiddenInput = document.getElementById('task-id')
    let pointsCounterText = document.getElementById('total-sprint-points')
    createBtn.addEventListener('click', createTask)

    let taskNum = 1
    let totalPoints = 0
    let allData = {}
    function createTask(e) {
        e.preventDefault()
        console.log(container)
        if (!title.value.trim() || !description.value.trim() || !label.value.trim() || !estimationPoints.value.trim() || !assignee.value.trim()) {
            return
        }
        allData = {
            title: title.value,
            description: description.value,
            label: label.value,
            estimationPoints: estimationPoints.value,
            assignee: assignee.value
        }

        totalPoints += Number(estimationPoints.value)
        pointsCounterText.textContent = `Total Points ${totalPoints}pts`
        let newArticle = document.createElement('article')
        let newDivLabel = document.createElement('div')
        let h3 = document.createElement('h3')
        let p = document.createElement('p')
        let newDivPoints = document.createElement('div')
        let newDivAssignee = document.createElement('div')
        let newDivActions = document.createElement('div')
        let delBtn = document.createElement('button')

        newArticle.classList = 'task-card'
        newArticle.id = `task-${taskNum}`
        hiddenInput.value = `task-${taskNum}`
        taskNum++
        if (taskNum > 3) {
            taskNum = 1
        }
        let classLabel = ''
        let sign = ''
        if (label.value === 'Feature') {
            classLabel = 'feature'
            sign = `⊡`
        } else if (label.value === 'Low Priority Bug') {
            classLabel = 'low-priority'
            sign = '☉'
        } else {
            classLabel = 'high-priority'
            sign ='⚠'
        }
        newDivLabel.classList.add('task-card-label', `${classLabel}`)
        h3.classList = 'task-card-title'
        p.classList = 'task-card-description'
        newDivPoints.classList = 'task-card-points'
        newDivAssignee.classList = 'task-card-assignee'
        newDivActions.classList = 'task-card-actions'

        newDivLabel.textContent = `${label.value} ${sign}`
        h3.textContent = title.value;
        p.textContent = description.value
        newDivPoints.textContent = `Estimated at ${estimationPoints.value} pts`
        newDivAssignee.textContent = `Assigned to: ${assignee.value}`
        delBtn.textContent = 'Delete'

        newArticle.appendChild(newDivLabel)
        newArticle.appendChild(h3)
        newArticle.appendChild(p)
        newArticle.appendChild(newDivPoints)
        newArticle.appendChild(newDivAssignee)
        newArticle.appendChild(newDivActions)
        newDivActions.appendChild(delBtn)
        container.appendChild(newArticle)
        title.value = ''
        description.value = ''
        label.value = ''
        estimationPoints.value = ''
        assignee.value = ''

        delBtn.addEventListener('click', delTask)

        function delTask() {
            title.value = allData.title
            description.value = allData.description
            label.value = allData.label
            estimationPoints.value = allData.estimationPoints
            assignee.value = allData.assignee
            deleteBtn.disabled = false
            createBtn.disabled = true
            title.disabled = true
            description.disabled = true
            label.disabled = true
            estimationPoints.disabled = true
            assignee.disabled = true
            deleteBtn.addEventListener('click', () => {
                totalPoints -= Number(estimationPoints.value)
                newArticle.remove()
                title.value = ''
                description.value = ''
                label.value = ''
                estimationPoints.value = ''
                assignee.value = ''
                deleteBtn.disabled = true
                createBtn.disabled = false
                title.disabled = false
                description.disabled = false
                label.disabled = false
                estimationPoints.disabled = false
                assignee.disabled = false
                pointsCounterText.textContent = `Total Points ${totalPoints}pts`
            })

        }
    }
}