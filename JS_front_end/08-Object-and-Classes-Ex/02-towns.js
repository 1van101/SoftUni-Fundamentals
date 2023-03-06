function solve(input) {
    let citiesInfo = [];
    
    for (const el of input) {
        let [city, latitude, longitude] = el.split(' | ');
        citiesInfo.push({town: city, latitude: Number(latitude).toFixed(2), longitude: Number(longitude).toFixed(2)});
    }

    for (const el of citiesInfo) {
        console.log(el)
    }
}

