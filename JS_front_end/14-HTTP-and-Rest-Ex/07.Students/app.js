function attachEvents() {
  const BASE_URL = 'http://localhost:3030/jsonstore/collections/students';
  let inputFields = Array.from(document.querySelectorAll('.inputs input'));
  let [fNameInput, lNameInput, facultyNumberInput, gradeInput] = inputFields
  let submitBtn = document.getElementById('submit')
  let tableBody = document.querySelector('#results tbody');

  addEventListener('load', loadData)
  submitBtn.addEventListener('click', createStudent);

  async function loadData() {
    tableBody.innerHTML = '';
    let response = await fetch(BASE_URL);
    let data = await response.json();

    for (const value of Object.values(data)) {
      let newRow = document.createElement('tr');
      let fNameCol = document.createElement('td');
      fNameCol.textContent = value.firstName;

      let lNameCol = document.createElement('td');
      lNameCol.textContent = value.lastName

      let facNumCol = document.createElement('td');
      facNumCol.textContent = value.facultyNumber

      let gradeCol = document.createElement('td');
      gradeCol.textContent = value.grade

      newRow.appendChild(fNameCol)
      newRow.appendChild(lNameCol)
      newRow.appendChild(facNumCol)
      newRow.appendChild(gradeCol)
      tableBody.appendChild(newRow)
    }
  }

  async function createStudent() {
    if (nonEmptyData(inputFields)) {
      fetch(BASE_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          firstName: fNameInput.value,
          lastName: lNameInput.value,
          facultyNumber: facultyNumberInput.value,
          grade: gradeInput.value,
        })
      })
      fNameInput.value = ''
      lNameInput.value = ''
      facultyNumberInput.value = ''
      gradeInput.value = ''
    }
  }

  function nonEmptyData(input){
    for (const item of input) {
      if (!item.value.trim()) {
        return false
      }
    }
    return true
  }
}
  attachEvents();