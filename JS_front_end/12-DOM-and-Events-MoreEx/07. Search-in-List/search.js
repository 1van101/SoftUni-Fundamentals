function search() {


   let towns = Array.from(document.querySelectorAll('#towns li'));
   towns.forEach((town) => {town.removeAttribute('style')});
   
   let input = document.querySelector('input[type="text"]').value;
   let result = document.getElementById('result');
   
   let occurrences = 0;

   for (const town of towns) {
      if (town.textContent.includes(input)) {
         occurrences++;
         town.style.fontWeight = 'bold';
         town.style.textDecoration = 'underline';
      }
   }

   result.textContent = `${occurrences} matches found`;
}
