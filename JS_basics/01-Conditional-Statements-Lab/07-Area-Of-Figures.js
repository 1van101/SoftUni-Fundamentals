function countingArea(input){
    
    areaCalculation = {
        'square': function(input) {return Number(input[1]) ** 2},
        'rectangle': function(input) {return Number(input[1]) * Number(input[2])},
        'circle': function(input) {return Math.PI * Number(input[1]) ** 2},
        'triangle': function(input) {return 0.5 * Number(input[1]) * Number(input[2])}
    };
    
    let type = input[0];
    console.log(areaCalculation[type](input));
};
