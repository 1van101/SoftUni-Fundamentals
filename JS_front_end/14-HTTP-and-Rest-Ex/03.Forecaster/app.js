function attachEvents() {
    let locationNameInput = document.getElementById('location');
    let submitBtn = document.getElementById('submit');
    let forecastSection = document.getElementById('forecast')
    let currentForecast = document.getElementById('current');
    let upcomingForecast = document.getElementById('upcoming');
    const BASE_URL = 'http://localhost:3030/jsonstore/forecaster/'


    let forecastSymbols = {
        'Sunny': '☀',
        'Partly sunny': '⛅',
        'Overcast': '☁',
        'Rain': '☂',
        'Degrees': '°'
    }

    submitBtn.addEventListener('click', getCodeLocation)
    async function getCodeLocation() {
        forecastSection.style.display = 'inline'
        try {
            let response = await fetch(`${BASE_URL}locations`)
            let data = await response.json();

            let searchedLocation = data.filter((e) => e.name === locationNameInput.value)[0]
            codeLoc = searchedLocation.code;

            getCurrentConditions()
            get3DayForecast()
        } catch (e) {
            forecastSection.innerHTML = 'Error'
        }

        async function getCurrentConditions() {
            let childToDelete = document.querySelector('.forecasts');
            if (childToDelete) {
                currentForecast.removeChild(childToDelete);
            }

            let response = await fetch(`${BASE_URL}today/${codeLoc}`);
            let data = await response.json();

            let newDiv = createElement('div', 'forecasts')
            currentForecast.appendChild(newDiv);

            let newSpanSymbol = createElement('span', 'condition symbol', forecastSymbols[data.forecast.condition])
            newDiv.appendChild(newSpanSymbol);

            let newSpanCondition = createElement('span', 'condition');
            newDiv.appendChild(newSpanCondition);

            let firstSpanForData = createElement('span', 'forecast-data', data.name);
            newSpanCondition.appendChild(firstSpanForData);

            let temperatureRange = `${data.forecast.low}°/${data.forecast.high}°`
            let secondSpanForData = createElement('span', 'forecast-data', temperatureRange);
            newSpanCondition.appendChild(secondSpanForData);

            let thirdSpanForData = createElement('span', 'forecast-data', data.forecast.condition);
            newSpanCondition.appendChild(thirdSpanForData);
        }

        async function get3DayForecast() {
            let childToDelete = document.querySelector('.forecast-info');
            if (childToDelete) {
                upcomingForecast.removeChild(childToDelete)
            }
            let response = await fetch(`${BASE_URL}upcoming/${codeLoc}`);
            let data = await response.json();

            let newDiv = createElement('div', 'forecast-info')
            upcomingForecast.appendChild(newDiv);

            for (const currentData of data.forecast) {
                let newSpanUpcoming = createElement('span', 'upcoming')

                let firstSpanSymbol = createElement('span', 'symbol', forecastSymbols[currentData.condition])
                newSpanUpcoming.appendChild(firstSpanSymbol);

                let temperatureRange = `${currentData.low}°/${currentData.high}°`
                let secondSpanSymbol = createElement('span', 'forecast-data', temperatureRange)
                newSpanUpcoming.appendChild(secondSpanSymbol);

                let thirdSpanSymbol = createElement('span', 'forecast-data', currentData.condition)
                newSpanUpcoming.appendChild(thirdSpanSymbol);
                newDiv.appendChild(newSpanUpcoming);
            }
        }
        function createElement(tag, classAdded, textAdded) {
            newEl = document.createElement(tag)
            newEl.className = classAdded
            newEl.textContent = textAdded
            return newEl
        }
    }
}

attachEvents();