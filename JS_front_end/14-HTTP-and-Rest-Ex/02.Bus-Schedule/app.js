function solve() {
    let info = document.querySelector('.info');
    let departBtn = document.getElementById('depart');
    let arriveBtn = document.getElementById('arrive');
    const BASE_URL = 'http://localhost:3030/jsonstore/bus/schedule/'
    let stop = 'depot';
    let name = '';

    async function depart() {
        departBtn.disabled = true;
        arriveBtn.disabled = false;

        try {
            let response = await fetch(`${BASE_URL}${stop}`)
            if (response.status === 204) {
                throw new Error()
            };
            
            let data = await response.json();
            name = data.name;
            stop = data.next;
            info.textContent = `Next stop ${name}`;
        } catch (e) {
            info.textContent = e
            departBtn.disabled = true;
            arriveBtn.disabled = true;
        }
    }

    function arrive() {
        departBtn.disabled = false;
        arriveBtn.disabled = true;
        info.textContent = `Arriving at ${name}`;
    }

    return {
        depart,
        arrive
    };
}

let result = solve();

