window.addEventListener('load', solve)

function solve() {
    let productName = document.getElementById('product');
    let countProducts = document.getElementById('count');
    let productPrice = document.getElementById('price');
    let addProductBtn = document.getElementById('add-product');
    let updateProductBtn = document.getElementById('update-product');
    let loadProductsBtn = document.getElementById('load-product');
    let productsContainer = document.getElementById('tbody')

    const BASE_URL = 'http://localhost:3030/jsonstore/grocery/'

    loadProductsBtn.addEventListener('click', loadAllProducts)
    addProductBtn.addEventListener('click', addProduct)

    async function loadAllProducts(e) {
        e?.preventDefault();
        productsContainer.innerHTML = '';
        let response = await fetch(BASE_URL)
        let data = await response.json();

        for (const info of Object.values(data)) {
            let product = info.product;
            let count = info.count;
            let price = info.price;
            let _id = info._id;

            let newRow = document.createElement('tr');
            let productCol = document.createElement('td');
            let countCol = document.createElement('td');
            let priceCol = document.createElement('td');
            let btnsCol = document.createElement('td');
            let updateBtn = document.createElement('button');
            let delBtn = document.createElement('button');

            productCol.textContent = product;
            countCol.textContent = count;
            priceCol.textContent = price;

            productCol.classList = 'name'
            countCol.classList = 'count-price'
            priceCol.classList = 'product-price'
            btnsCol.classList = 'btn';
            updateBtn.classList = 'update';
            delBtn.classList = 'delete';


            updateBtn.textContent = 'Update';
            delBtn.textContent = 'Delete';

            btnsCol.appendChild(updateBtn);
            btnsCol.appendChild(delBtn);

            newRow.appendChild(productCol);
            newRow.appendChild(countCol);
            newRow.appendChild(priceCol);
            newRow.appendChild(btnsCol)
            productsContainer.appendChild(newRow);

            delBtn.addEventListener('click', () => deleteProduct(_id));
            updateBtn.addEventListener('click', () => updateProduct(_id, product, count, price));
        }

    }

    async function addProduct(e) {
        e.preventDefault();

        let product = productName.value;
        let count = countProducts.value;
        let price = productPrice.value;

        if (!product.trim() || !count.trim() || !price.trim()) {
            return
        }

        let httpHeaders = {
            method: 'POST',
            body: JSON.stringify({
                product,
                count,
                price
            })
        }
        await fetch(BASE_URL, httpHeaders)
        productName.value = '';
        countProducts.value = '';
        productPrice.value = '';
        loadAllProducts()
    }

    async function deleteProduct(id) {
        await fetch(BASE_URL + id, { method: 'DELETE' })
        loadAllProducts()
    }

    async function updateProduct(id, product, count, price) {
        addProductBtn.disabled = true
        updateProductBtn.disabled = false

        productName.value = product;
        countProducts.value = count;
        productPrice.value = price;
        
        if (
            !productName.value.trim() ||
            !countProducts.value.trim() ||
            !productPrice.value.trim()
        ) {
            return
        }
        
        updateProductBtn.addEventListener('click', async () => {
            httpHeaders = {
                method: 'PATCH',
                body: JSON.stringify({
                    product: productName.value,
                    count: countProducts.value,
                    price: productPrice.value
                })
            }
            await fetch(BASE_URL + id, httpHeaders)
            
            addProductBtn.disabled = false
            updateProductBtn.disabled = true
            
            productName.value = '';
            countProducts.value = '';
            productPrice.value = '';
            
            loadAllProducts()
        })

    }
}