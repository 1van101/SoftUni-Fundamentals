function solve(str){
    let pattern = '([A-Z][a-z]*)';
    let output = []
    let matches = str.matchAll(pattern);
    
    for (let word of matches){
        output.push(word[0])
    }

    console.log(output.join(', '))
}
