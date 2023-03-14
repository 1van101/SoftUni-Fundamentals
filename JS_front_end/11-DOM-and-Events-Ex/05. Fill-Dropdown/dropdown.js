function addItem() {
    let target = document.getElementById('menu');

    let newText = document.getElementById('newItemText');
    let newValue = document.getElementById('newItemValue');

    let newOption = document.createElement('option');
    newOption.textContent = newText.value;
    newOption.value = newValue.value;

    target.appendChild(newOption);

    newText.value = '';
    newValue.value = '';
}