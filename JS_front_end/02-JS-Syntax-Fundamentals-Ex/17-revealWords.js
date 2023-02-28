function solve(words, text) {
    let wordsArr = words.split(', ');

    while (wordsArr.length > 0) {
        let currentWord = wordsArr.shift();
        let wordToReplace = '*'.repeat(currentWord.length);

        text = text.replace(wordToReplace, currentWord);
    }
    console.log(text)
}


