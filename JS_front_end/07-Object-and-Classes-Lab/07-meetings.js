function meetingAppointments(input){
    let meetings = {};
    for (const el of input) {
        let [day, name] = el.split(' ');
        
        if (day in meetings){
            console.log(`Conflict on ${day}!`)
        }else{
            meetings[day] = name;
            console.log(`Scheduled for ${day}`)
        }
    }

    for (const day of Object.keys(meetings)) {
        console.log(`${day} -> ${meetings[day]}`);
    }
}

