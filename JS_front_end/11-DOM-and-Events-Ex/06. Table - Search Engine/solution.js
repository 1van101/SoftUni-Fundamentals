function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      let rows = document.querySelectorAll('tbody tr');

      for (const iterator of rows) {
         iterator.classList.remove('select')
      }
      
      let searchWord = document.getElementById('searchField');

      for (const el of rows) {
         if ((el.innerText.includes(searchWord.value)) && (searchWord.value.length > 0)){
            el.className = 'select'
         }
      }
      searchWord.value = ''
   }
}




