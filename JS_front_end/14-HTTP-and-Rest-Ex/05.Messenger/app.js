function attachEvents() {
    let submitBtn = document.getElementById('submit');
    let refreshBtn = document.getElementById('refresh');
    let [author, content] = document.querySelectorAll('#controls input');
    let textArea = document.getElementById('messages')
    const BASE_URL = 'http://localhost:3030/jsonstore/messenger';

    submitBtn.addEventListener('click', () => {
        fetch(BASE_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                "author": author.value,
                "content": content.value
            })
        });
    });

    refreshBtn.addEventListener('click', getAllMessages)

    async function getAllMessages(){
        let response = await fetch(BASE_URL);
        let data = await response.json();
        
        let output = []
        
        for (const value of Object.values(data)) {
            output.push(`${value.author}: ${value.content}`)
        }
        
        textArea.textContent = output.join('\n')
    }
}

attachEvents();