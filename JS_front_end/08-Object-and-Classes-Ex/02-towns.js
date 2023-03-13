function solve(input) {
    let citiesInfo = [];
    
    for (const el of input) {
        let [town, latitude, longitude] = el.split(' | ');
        citiesInfo.push({town: town, latitude: Number(latitude).toFixed(2), longitude: Number(longitude).toFixed(2)});
    }

    for (const el of citiesInfo) {
        console.log(el)
    }
}

    // input
    //   .map((line) => line.split(' | '))
    //   .map(([town, latitude, longitude]) => ({town: town, latitude: Number(latitude).toFixed(2), longitude: Number(longitude).toFixed(2)}))
    //   .forEach((townObj) => console.log(townObj));
