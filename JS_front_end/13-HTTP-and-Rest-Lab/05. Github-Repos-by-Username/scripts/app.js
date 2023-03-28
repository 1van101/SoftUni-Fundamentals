async function loadRepos() {

	const input = document.getElementById('username').value;
	const repos = document.getElementById('repos');
	const BASE_URL = 'https://api.github.com/users';
	repos.innerHTML = '';
	
	try{
		let response = await fetch(`${BASE_URL}/${input}/repos`);
		if (!response.ok && response.status === 404){
            throw new Error(`${response.status} (Not Found)`);
        }
		let data = await response.json();
		
		data.forEach(element => {
			let newLi = document.createElement('li')
			let newA = document.createElement('a')
			
			newA.href = element.html_url
			newA.textContent = element.full_name
			newLi.appendChild(newA)
			repos.appendChild(newLi)
		});
	}catch (error) {
        let newLi = document.createElement('li');
        newLi.textContent = error
        repos.appendChild(newLi);
	}
}