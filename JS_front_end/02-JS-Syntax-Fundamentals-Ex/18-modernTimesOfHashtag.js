function solve(text){
    let regEx = /#([A-Za-z]+)/g;
    let matches = text.match(regEx);
    
    for (let i = 0; i < matches.length; i++){
        console.log(matches[i].slice(1));
    }
}
