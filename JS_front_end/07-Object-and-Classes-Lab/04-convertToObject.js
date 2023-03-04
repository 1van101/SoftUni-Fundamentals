function JSONToObject(obj){
    let newObject = JSON.parse(obj);
    
    for (let el of Object.keys(newObject)) {
        console.log(`${el}: ${newObject[el]}`)
    }
}

JSONToObject('{"name": "George", "age": 40, "town": "Sofia"}')