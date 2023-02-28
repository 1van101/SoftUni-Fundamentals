function solve(word, text){
    let pattern = `\\b${word}\\b`;
    let re = new RegExp(pattern, 'i');

    let output = re.test(text); 
    
    if (output == true){
        console.log(word)
    }else{
        console.log(`${word} not found!`)
    }
}



solve('javascript',
'Javascripts is the best apython , language'
)
