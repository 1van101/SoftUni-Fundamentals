function solve() {
  let inputElements = document.getElementById('input')
    .value
    .split('.')
    .filter(el => el !== '');

  let output = document.getElementById('output'); 
  
  while (inputElements.length > 0){
    let paragraphText = (inputElements.splice(0, 3)).join('.') + '.';
    output.innerHTML += `<p>${paragraphText}</p>`;
  }
}