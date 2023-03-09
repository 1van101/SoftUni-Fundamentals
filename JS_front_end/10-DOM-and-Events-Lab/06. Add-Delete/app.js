function addItem() {
    let newItem = document.getElementById("newItemText").value;

    let newLi = document.createElement('li');
    newLi.textContent = newItem;

    let deleteLink = document.createElement('a');
    deleteLink.appendChild(document.createTextNode('[Delete]'));
    deleteLink.href = '#';
    newLi.appendChild(deleteLink);


    let list = document.getElementById('items');
    list.appendChild(newLi)

    deleteLink.addEventListener('click', () => newLi.parentElement.removeChild(newLi))

}