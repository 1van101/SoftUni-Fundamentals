function solve() {
  let buttons = document.querySelectorAll('#exercise button');

  let generateButton = buttons[0];
  let buyButton = buttons[1];

  let textAreas = document.querySelectorAll('textarea');
  let outputField = textAreas[1];
  let tableBody = document.querySelector('tbody');

  generateButton.addEventListener('click', addData);
  buyButton.addEventListener('click', buyProducts);

  function addData() {

    let inputData = JSON.parse(textAreas[0].value);

    for (const currentProduct of inputData) {
      let newTableRow = document.createElement('tr');
      let colImage = `<td><img src="${currentProduct['img']}"></td>`;
      let colName = `<td><p>${currentProduct['name']}</p></td>`;
      let colPrice = `<td><p>${currentProduct['price']}</p></td>`;
      let colDFactor = `<td><p>${currentProduct['decFactor']}</p></td>`;
      let colMark = `<td><input type="checkbox"/></td>`;

      newTableRow.innerHTML = colImage + colName + colPrice + colDFactor + colMark
      tableBody.appendChild(newTableRow);
    }
  }

  function buyProducts() {
    let boughtProductsNames = []
    let totalPrice = 0
    let totalDecFactor = 0

    for (const product of tableBody.querySelectorAll('tr')) {

      let [_productPicture,
        productName,
        productPrice,
        productFactor,
        markStatus
      ] = product.querySelectorAll('td');


      if (markStatus.children[0].checked) {
        boughtProductsNames.push(productName.textContent);
        totalPrice += parseFloat(productPrice.textContent);
        totalDecFactor += parseFloat(productFactor.textContent);
      }
    }

    if (boughtProductsNames.length > 0) {
      outputField.value = `Bought furniture: ${boughtProductsNames.join(", ")}\nTotal price: ${totalPrice.toFixed(2)}\nAverage decoration factor: ${totalDecFactor / boughtProductsNames.length}`
    }

  }
}