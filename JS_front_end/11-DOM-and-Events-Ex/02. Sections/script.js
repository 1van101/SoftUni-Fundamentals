function create(words) {
   for (const el of words) {
      let target = document.getElementById('content')
      let currentSection = document.createElement('div');
      
      let p = document.createElement('p');
      p.textContent = el;
      p.style.display = 'none';
      
      currentSection.appendChild(p)
      target.appendChild(currentSection);
   };

   let divElements = document.querySelectorAll('#content div')

   for (const div of divElements){
      div.addEventListener('click', display)
   }

   function display(el){
      currentEl = el.currentTarget.firstChild;
      let condition = currentEl.style.display;
      currentEl.style.display = (condition === 'none') ? 'block' : 'none';
   }
}