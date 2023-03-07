function solve(ch1, ch2) {
    let start = ch1.charCodeAt();
    let end = ch2.charCodeAt();
    let res = '';

    if (start > end) {
        [start, end] = [end, start];
    }

    for (let i = start + 1; i < end; i++) {
        res += String.fromCharCode(i) + ' ';
    }

    console.log(res.trim())
}

solve('a', 'z')