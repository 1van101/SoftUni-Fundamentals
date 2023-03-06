function solve(input) {
    let countOccurrences = {}
    let [searchedWords, ...words] = input;
    
    for (const word of searchedWords.split(' ')) {
        countOccurrences[word] = 0;
    }

    for (const el of words) {
        if (Object.keys(countOccurrences).includes(el)){
            countOccurrences[el]+= 1;
        }
    }

    let countOccurrencesSorted = Object.entries(countOccurrences).sort((a, b) => b[1] - a[1])

    for (const [word, occurrences] of countOccurrencesSorted) {
        console.log(`${word} - ${occurrences}`)
    }
}

solve([
    'is the', 
    'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence']
    
    )