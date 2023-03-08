function extractText() {
    let result = document.getElementById('result');

    let elements = document.querySelectorAll("#items li");

    for (const el of elements) {
        result.value += el.textContent + '\n'
    }
}