function solve(input) {
    products = input.shift().split('!');

    function productExists(p) {
        return products.includes(p)
    }

    for (const line of input) {
        if (line === 'Go Shopping!'){
            break;
        }

        let tokens = line.split(' ');
        let command = tokens[0];
        
        if (command === 'Urgent' && !productExists(tokens[1])) {
            products.unshift(tokens[1]);
        }else if (command === 'Unnecessary' && productExists(tokens[1])) {
            let index = products.indexOf(tokens[1]);
            products.splice(index, 1)
        }else if (command === 'Correct' && productExists(tokens[1])) {
            let indexOld = products.indexOf(tokens[1])
            products[indexOld] = tokens[2];
        }else if (command === 'Rearrange' && productExists(tokens[1])) {
            products.splice(products.indexOf(tokens[1]), 1)
            products.push(tokens[1])
        }
    }
    console.log(products.join(', '));
}

