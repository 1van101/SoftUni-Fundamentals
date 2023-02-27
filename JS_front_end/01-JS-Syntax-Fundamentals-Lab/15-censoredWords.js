function censoredWords(sentence, word){
    console.log(sentence.split(word).join('*'.repeat(word.length)));
}
