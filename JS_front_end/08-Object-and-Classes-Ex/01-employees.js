function solve(input){
    let names = {};
    for (const name of input) {
        names[name] = name.length;
    }

    for (const el of Object.keys(names)) {
        console.log(`Name: ${el} -- Personal Number: ${names[el]}`)
    }
}