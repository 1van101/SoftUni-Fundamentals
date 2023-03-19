function extract(content) {
    let result = document.getElementById(content).textContent;
    let matches = result
        .match(/\(([^()]+)\)/g)
        .map(x => x.slice(1, x.length - 1))
        .join('; ');

    return matches;
}