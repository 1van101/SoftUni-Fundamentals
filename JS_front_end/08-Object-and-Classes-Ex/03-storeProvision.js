function solve(currentProducts, orderedProducts) {
    let provisions = {};

    function add(arr) {
        for (let i = 0; i < arr.length; i += 2) {
            product = arr[i];
            qty = Number(arr[i + 1]);

            if (!provisions.hasOwnProperty(product)) {
                provisions[product] = 0;
            }
            provisions[product] += qty;
        }
    }

    add(currentProducts);
    add(orderedProducts);

    for (const el of Object.keys(provisions)) {
        console.log(`${el} -> ${provisions[el]}`)
    }
}

