// 'Kiril:BOP-1209:Fix Minor Bug:ToDo:3'


function solve(input) {
    let lines = Number(input.shift());

    let data = {}
    for (let i = 0; i < lines; i++) {
        let currentLine = input.shift();
        let [assignee, taskId, title, status, points] = currentLine.split(':')

        if (!data.hasOwnProperty(assignee)) {
            data[assignee] = []
        }
        data[assignee].push({taskId:taskId, content: [title, status, points]})
    }

    while (input.length > 0) {
        let currentLine = input.shift().split(':')
        let command = currentLine[0]
        if (command === 'Add New'){
            let assignee = currentLine[1]
            let taskId = currentLine[2]
            let title = currentLine[3]
            let status = currentLine[4]
            let points = Number(currentLine[5])
            if(!data.hasOwnProperty(assignee)){
                console.log(`Assignee ${assignee} does not exist on the board!`)
            }else{
                data[assignee].push({taskId:taskId, content: [title, status, points]})
            }

        }else if (command === 'Change Status'){
            let assignee = currentLine[1]
            let taskId = currentLine[2]
            let newStatus = currentLine[3]
            let exist = false
            if(!data.hasOwnProperty(assignee)){
                console.log(`Assignee ${assignee} does not exist on the board!`)
            }else{
                for (const task of data[assignee]) {
                    if(task.taskId === taskId){
                        exist = true
                        task.content[1] = newStatus
                    }
                    
                }
                if (!exist){
                    console.log(`Task with ID ${taskId} does not exist for ${assignee}!`)
                }
            }
        }else if(command ==='Remove Task'){
            let assignee = currentLine[1]
            let index = Number(currentLine[2])
            if(!data.hasOwnProperty(assignee)){
                console.log(`Assignee ${assignee} does not exist on the board!`)
            }else{
            
                if(index >= data[assignee].length || index < 0){
                    console.log("Index is out of range!")
                }else{
                    data[assignee].splice(index, 1)
                }
            }
        }
    }
    let toDoPoints = 0
    let inProgressPoints = 0
    let codeReviewPoints = 0
    let donePoints = 0

    for (const container of Object.values(data)) {
        for (const task of Object.values(container)) {
            if (task.content[1] === 'ToDo'){
                toDoPoints += Number(task.content[2])
            }else if(task.content[1] === 'In Progress'){
                inProgressPoints += Number(task.content[2])
            }else if(task.content[1] === 'Code Review'){
                codeReviewPoints += Number(task.content[2])
            }else if (task.content[1] === 'Done'){
                donePoints += Number(task.content[2])
            }
        }
    }

    console.log(`ToDo: ${toDoPoints}pts`)
    console.log(`In Progress: ${inProgressPoints}pts`)
    console.log(`Code Review: ${codeReviewPoints}pts`)
    console.log(`Done Points: ${donePoints}pts`)

    if (donePoints >= toDoPoints + inProgressPoints + codeReviewPoints ){
        console.log('Sprint was successful!')
    }else(
        console.log('Sprint was unsuccessful...')
    )
}

solve(    [
    '5',
    'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
    'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
    'Peter:BOP-1211:POC:Code Review:5',
    'Georgi:BOP-1212:Investigation Task:Done:2',
    'Mariya:BOP-1213:New Account Page:In Progress:13',
    'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
    'Change Status:Peter:BOP-1290:ToDo',
    'Remove Task:Mariya:1',
    'Remove Task:Joro:1',
]

)