function solve(speed, area){
    
    let areasLimits = {
        'motorway': 130,
        'interstate': 90,
        'city': 50,
        'residential': 20
    };

    let speedLimit = areasLimits[area];

    if (speed > speedLimit){
        let diff = speed - speedLimit;
        let status = '';

        if (diff <= 20){
            status = 'speeding';
        }else if (diff <= 40){
            status = 'excessive speeding';
        }else{
            status = 'reckless driving';
        }

        console.log(`The speed is ${diff} km/h faster than the allowed speed of ${speedLimit} - ${status}`);
    }else{
        console.log(`Driving ${speed} km/h in a ${speedLimit} zone`);
    }
}
