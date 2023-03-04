function solve(input){
    peopleData = {}
    for (const data of input) {
        let [name, number] = data.split(' ');
        
        peopleData[name] = number;
    }
    
    for (const personName of Object.keys(peopleData)) {
        console.log(`${personName} -> ${peopleData[personName]}`);
    }
}

solve(['Tim 0834212554',
'Peter 0877547887',
'Bill 0896543112',
'Tim 0876566344']
)