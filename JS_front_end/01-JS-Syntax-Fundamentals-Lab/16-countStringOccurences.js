function occurrences(string, word){
    let count = 0;
    let stringArr = string.split(' ');

    for(let w of stringArr){
        if (w === word){
            count++;
        }
    }
    console.log(count)
}

occurrences('softuni is great place for learning new programming languages',
'softuni'

)