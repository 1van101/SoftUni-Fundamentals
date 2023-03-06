function solve(input){
    let heroes = [];

    for (const el of input) {
        let [heroName, level, items] = el.split(' / ');
        heroes.push({name: heroName, level: level, items: items});
    }

    heroes.sort((a, b) => a.level - b.level);

    for (const hero of heroes) {
        console.log(`Hero: ${hero.name}\nlevel => ${hero.level}\nitems => ${hero.items}`);
    }
}

solve([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 24 / BarrelVest, DestructionSword',
    'Hes / 3 / Desolator, Sentinel, Antara'
    ]
    )