function solve() {

  let input = document.getElementById('text').value.toLowerCase();
  let currentCase = document.getElementById('naming-convention').value;
  let result = document.getElementById('result');

  switch (currentCase) {
    case 'Camel Case': result.textContent = input.replace(/[^a-zA-Z0-9]+(.)/g, (m, chr) => chr.toUpperCase()); break;
    case 'Pascal Case': result.textContent = (' ' + input).replace(/[^a-zA-Z0-9]+(.)/g, (m, chr) => chr.toUpperCase()); break;
    default: result.textContent = 'Error!'
  }
}