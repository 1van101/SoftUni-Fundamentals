function colorize() {
    let rows = document.querySelectorAll('table tr:nth-child(even)');
    for (const el of rows) {
        el.style.backgroundColor = 'Teal';
    }
}