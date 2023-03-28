async function loadRepos() {
   const BASIC_URL = 'https://api.github.com/users/testnakov/repos';
   const result = document.getElementById('res');
   try {
      const response = await fetch(BASIC_URL)
      if (!response.ok && response.status === 404) {
         throw new Error(`${response.status} - Not Found`);
      }
      const data = await response.text()
      result.textContent = data

   } catch (error) {
      result.textContent = error
   }


}