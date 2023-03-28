async function loadCommits() {
    // https://api.github.com/repos/<username>/<repository>/commits
    const username = document.getElementById('username').value;
    const repo = document.getElementById('repo').value;
    const commits = document.getElementById('commits');

    const BASE_URL = 'https://api.github.com/repos';
    commits.innerHTML = '';
    try {
        let response = await fetch(`${BASE_URL}/${username}/${repo}/commits`);
        if (!response.ok && response.status === 404){
            throw new Error(`${response.status} (Not Found)`);
        }
        let data = await response.json();

        data.forEach(c => {
            let newLi = document.createElement('li');
            console.log(c.commit.author.name)
            newLi.textContent = `${c.commit.author.name}: ${c.commit.message}`
            commits.appendChild(newLi);
        });

    } catch (error) {
        let newLi = document.createElement('li');
        newLi.textContent = error
        commits.appendChild(newLi);
    }

}