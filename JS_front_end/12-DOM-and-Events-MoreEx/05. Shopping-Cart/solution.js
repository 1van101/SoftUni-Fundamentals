function solve() {
   let boughtProducts = new Set();
   let totalPrice = 0;

   const addButtons = Array.from(document.querySelectorAll('.add-product'));
   const textArea = document.querySelector('textarea');
   const checkoutButton = document.querySelector('.checkout')

   addButtons.forEach(button => button.addEventListener('click', addProduct));
   checkoutButton.addEventListener('click', buyProducts)

   function addProduct(event) {
      const parent = event.currentTarget.parentElement.parentElement;
      let productName = parent.querySelector('.product-title').textContent;
      let productPrice = Number(parent.querySelector('.product-line-price').textContent);

      totalPrice += productPrice;
      boughtProducts.add(productName);

      textArea.value += `Added ${productName} for ${Number(productPrice).toFixed(2)} to the cart.\n`;
   }

   function buyProducts() {
      textArea.value += `You bought ${Array.from(boughtProducts).join(', ')} for ${totalPrice.toFixed(2)}.`
      addButtons.forEach(button => button.disabled = true);
      checkoutButton.disabled = true;
   }
}
