function solve(input){
    let parkingData = new Set();
    
    let commands = {
        'IN': function(num){parkingData.add(num)},
        'OUT': function(num){parkingData.delete(num)}
    }
    for (const el of input) {
        let [command, number] = el.split(', ');
        commands[command](number);
    }
    
    if (parkingData.length === 0){
        console.log('Parking Lot is Empty');
    }else{
        console.log([...parkingData].sort().join('\n'));
    }
}

solve(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'IN, CA9999TT',
'IN, CA2866HI',
'OUT, CA1234TA',
'IN, CA2844AA',
'OUT, CA2866HI',
'IN, CA9876HH',
'IN, CA2822UU']
)