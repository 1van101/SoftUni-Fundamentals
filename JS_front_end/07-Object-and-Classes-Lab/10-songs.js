function solve(input) {
    let type = input.pop();
    let songsInfo = input.slice(1);
    let songs = [];

    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }

    for (const el of songsInfo) {
        let [songType, songName, songLength] = el.split('_');
        songs.push(new Song(songType, songName, songLength));
    }

    let filteredSongs = songs.filter(s => s.typeList == type || type == 'all');
    for (const song of filteredSongs) {
        console.log(song.name);
    }
}

solve([4,
    'favourite_DownTown_3:14',
    'listenLater_Andalouse_3:24',
    'favourite_In To The Night_3:58',
    'favourite_Live It Up_3:48',
    'all']

)