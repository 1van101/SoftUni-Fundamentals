function solve(string) {
    let occurrences = {};
    let words = string.split(' ');

    while (words.length > 0) {
        let currWord = words.shift().toLowerCase();
        if (!occurrences.hasOwnProperty(currWord)) {
            occurrences[currWord] = 0;
        }
        occurrences[currWord] += 1;
    }

    let oddOccurrences = Object.keys(occurrences).filter(x => occurrences[x] % 2 != 0)
    console.log(oddOccurrences.join(' '))
}
solve('Cake IS SWEET is Soft CAKE sweet Food')