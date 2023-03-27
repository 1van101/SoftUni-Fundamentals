async function getInfo() {
    let inputId = document.getElementById('stopId').value;
    const BASE_URL = 'http://localhost:3030/jsonstore/bus/businfo/';
    const stopName = document.getElementById('stopName');
    const busesList = document.getElementById('buses')
    busesList.innerHTML = '';
    stopName.innerHTML = '';
    
    try{
        let response = await fetch(`${BASE_URL}${inputId}`);
        let data = await response.json();
        
        stopName.textContent = data.name;
        for (const [busId, time] of Object.entries(data.buses)) {
            let newLi = document.createElement('li')
            newLi.textContent = `Bus ${busId} arrives in ${time} minutes`;
            busesList.appendChild(newLi);
        }
    }catch(e){
        stopName.textContent = "Error";
    }
}