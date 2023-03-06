function solve(input){
    let moviesInfo = [];

    function addMovie(name){
        moviesInfo.push({"name": name});
    }
    function addDirector(movieName, director){
        for (const movie of moviesInfo) {
            if (movie["name"] === movieName){
                movie["director"] = director;
            }
        }
    }

    function addDate(movieName, date){
        for (const movie of moviesInfo) {
            if (movie["name"] === movieName){
                movie["date"] = date;
            }
        }
    }

    for (const el of input) {
        if (el.includes('addMovie')){
            currData = el.split(' ')
            let movie = (currData.slice(1)).join(' ')
            addMovie(movie)
        }else if (el.includes('directedBy')){
            let [movie, director] = el.split(' directedBy ');
            addDirector(movie, director);
        }else if (el.includes('onDate')){
            let [movie, date] = el.split(' onDate ');
            addDate(movie, date)
        }
    }

    for (const iterator of moviesInfo) {
        if(Object.values(iterator).length === 3){
            console.log(JSON.stringify(iterator))
        }
    }
}

solve([
    'addMovie The Avengers',
    'addMovie Superman',
    'The Avengers directedBy Anthony Russo',
    'The Avengers onDate 30.07.2010',
    'Captain America onDate 30.07.2010',
    'Captain America directedBy Joe Russo'
    ]
    
    )