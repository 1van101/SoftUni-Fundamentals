window.addEventListener('load', solve);

function solve(e) {
    let inputs = Array.from(document.querySelectorAll('input'))
    let [fname, lname, checkIn, checkOut, guests] = inputs
    let nextBtn = document.getElementById('next-btn')
    let reservationInfoContainer = document.querySelector('.info-list')
    let confirmReservationContainer = document.querySelector('.confirm-list')
    let verificationText = document.getElementById('verification')
    let allData = {}

    nextBtn.addEventListener('click', reservationPreview);

    function reservationPreview(e) {
        e.preventDefault();
        console.log(checkIn.value)
        let checkInDate = new Date(Date.parse(checkIn.value.replace(/-/g, " ")));
        let checkOutDate = new Date(Date.parse(checkOut.value.replace(/-/g, " ")));
        if (
            (!fname.value.trim() || !lname.value.trim() || !checkIn.value.trim() || !checkOut.value.trim() || !guests.value.trim())
        ) {
            return
        }

        if (checkInDate < checkOutDate) {
            nextBtn.disabled = true
            allData = {
                fname: fname.value,
                lname: lname.value,
                checkIn: checkIn.value,
                checkOut: checkOut.value,
                guests: guests.value
            }
            let newLi = document.createElement('li')
            let newArticle = document.createElement('article')
            let newH3 = document.createElement('h3')
            let newPCheckIn = document.createElement('p')
            let newPCheckOut = document.createElement('p')
            let newPPeopleCount = document.createElement('p')
            let editBtn = document.createElement('button')
            let continueBtn = document.createElement('button')

            newLi.classList = 'reservation-content'
            editBtn.classList = 'edit-btn'
            continueBtn.classList = 'continue-btn'

            newH3.textContent = `Name: ${fname.value} ${lname.value}`
            newPCheckIn.textContent = `From date: ${checkIn.value}`
            newPCheckOut.textContent = `To date: ${checkOut.value}`
            newPPeopleCount.textContent = `For ${guests.value} people`
            editBtn.textContent = 'Edit'
            continueBtn.textContent = 'Continue'

            newArticle.appendChild(newH3)
            newArticle.appendChild(newPCheckIn)
            newArticle.appendChild(newPCheckOut)
            newArticle.appendChild(newPPeopleCount)
            newLi.appendChild(newArticle)
            newLi.appendChild(editBtn)
            newLi.appendChild(continueBtn)

            reservationInfoContainer.appendChild(newLi)
            clearInput()

            editBtn.addEventListener('click', () => {
                reservationInfoContainer.innerHTML = '';
                fname.value = allData.fname
                lname.value = allData.lname
                checkIn.value = allData.checkIn
                checkOut.value = allData.checkOut
                guests.value = allData.guests
                nextBtn.disabled = false
            })

            continueBtn.addEventListener('click', () => {
                confirmReservationContainer.appendChild(newLi)
                reservationInfoContainer.innerHTML = '';
                editBtn.remove()
                continueBtn.remove()
                let confirmBtn = document.createElement('button')
                let cancelBtn = document.createElement('button')
                
                confirmBtn.classList = 'confirm-btn'
                cancelBtn.classList = 'cancel-btn'

                confirmBtn.textContent = "Confirm"
                cancelBtn.textContent = "Cancel"

                newLi.appendChild(confirmBtn)
                newLi.appendChild(cancelBtn)

                confirmBtn.addEventListener("click", confirmReservation)
                cancelBtn.addEventListener("click", cancelReservation)
            })
            function confirmReservation(){
                nextBtn.disabled = false
                newLi.remove()
                verificationText.textContent = 'Confirmed.'
                verificationText.classList = 'reservation-confirmed'
            }

            function cancelReservation(){
                newLi.remove()
                nextBtn.disabled = false
                verificationText.textContent = 'Cancelled.'
                verificationText.classList = 'reservation-cancelled'
            }

        }
    }
    function clearInput() {
        inputs.forEach(el => el.value = '')
    }
}



