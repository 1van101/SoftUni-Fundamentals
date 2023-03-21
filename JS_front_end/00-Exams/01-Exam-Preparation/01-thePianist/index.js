function solve(input) {
    const lines = input.shift();
    let collection = {}

    for (let i = 0; i < lines; i++) {
        let [piece, composer, key] = input.shift().split('|');
        collection[piece] = { composer, key }
    }

    input.forEach(i => {
        let currentLine = i.split('|');
        let currentCase = currentLine[0];

        switch (currentCase) {
            case 'Add': addPiece(currentLine[1], currentLine[2], currentLine[3]); break;
            case 'Remove': removePiece(currentLine[1]); break;
            case 'ChangeKey': changeKey(currentLine[1], currentLine[2]); break;
        }
    })

    Object.keys(collection).forEach(el => console.log(`${el} -> Composer: ${collection[el].composer}, Key: ${collection[el].key}`));

    function addPiece(piece, composer, key) {
        if (piece in collection) {
            console.log(`${piece} is already in the collection!`);
        } else {
            collection[piece] = { composer, key };
            console.log(`${piece} by ${composer} in ${key} added to the collection!`);
        }
    };

    function removePiece(piece) {
        if (piece in collection) {
            delete collection[piece];
            console.log(`Successfully removed ${piece}!`);
        } else {
            console.log(`Invalid operation! ${piece} does not exist in the collection.`);
        }

    };

    function changeKey(piece, newKey) {
        if (piece in collection) {
            collection[piece].key = newKey;
            console.log(`Changed the key of ${piece} to ${newKey}!`);
        } else {
            console.log(`Invalid operation! ${piece} does not exist in the collection.`);
        }
    }

}

solve([
    '4',
    'Eine kleine Nachtmusik|Mozart|G Major',
    'La Campanella|Liszt|G# Minor',
    'The Marriage of Figaro|Mozart|G Major',
    'Hungarian Dance No.5|Brahms|G Minor',
    'Add|Spring|Vivaldi|E Major',
    'Remove|The Marriage of Figaro',
    'Remove|Turkish March',
    'ChangeKey|Spring|C Major',
    'Add|Nocturne|Chopin|C# Minor',
    'Stop'
]

)