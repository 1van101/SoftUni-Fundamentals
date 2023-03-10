function sumTable() {
    let prices = document.querySelectorAll('tbody tr td:nth-child(even)');
    let totalSum = 0;
    
    for (const price of prices) {
        totalSum += Number(price.textContent)
    }

    let totalSumCell = document.getElementById('sum');
    totalSumCell.textContent = totalSum
}