function solve(fName, lName, hairColor){
    let person = {
        name: fName,
        lastName: lName,
        hairColor: hairColor
    }

    let personJSON = JSON.stringify(person)
    console.log(personJSON)
}