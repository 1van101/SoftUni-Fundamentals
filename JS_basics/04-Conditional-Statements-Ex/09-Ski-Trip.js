function skiTripPrice(input) {
    let nights = Number(input[0]) - 1;
    let typeRoom = input[1];
    let rating = input[2];
    let totalPrice = 0

    switch (typeRoom) {
        case ('room for one person'): totalPrice = nights * 18; break;
        case ('apartment'): totalPrice = nights * 25;
            if (nights < 10) {
                totalPrice *= 0.7;
            } else if (nights <= 15) {
                totalPrice *= 0.65;
            } else {
                totalPrice *= 0.5;
            }
            break;
        case ('president apartment'): totalPrice = nights * 35;
            if (nights < 10) {
                totalPrice *= 0.9;
            } else if (nights <= 15) {
                totalPrice *= 0.85;
            } else {
                totalPrice *= 0.8;
            }
            break;
    }

    switch (rating) {
        case ('positive'): totalPrice *= 1.25; break;
        case ('negative'): totalPrice *= 0.9; break;
    }
    console.log(totalPrice.toFixed(2))
}

skiTripPrice(["30",
    "president apartment",
    "negative"])
