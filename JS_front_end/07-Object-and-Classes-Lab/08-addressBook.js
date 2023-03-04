function addressBook(input){
    let peopleInformation = {};
    
    for (const el of input) {
        let [name, address] = el.split(':');

        peopleInformation[name] = address;
    }
    let sortedAddressBook = Object.keys(peopleInformation).sort();

    for (const name of sortedAddressBook) {
        console.log(`${name} -> ${peopleInformation[name]}`);
    }
};

