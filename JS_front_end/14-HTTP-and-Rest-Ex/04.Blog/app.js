function attachEvents() {
    let btnLoadPosts = document.getElementById('btnLoadPosts');
    let btnViewPost = document.getElementById('btnViewPost');
    let posts = document.getElementById('posts');
    let postTitle = document.getElementById('post-title');
    let postBody = document.getElementById('post-body');
    let commentsContainer = document.getElementById('post-comments');
    const BASE_URL = 'http://localhost:3030/jsonstore/blog/';

    let postsWithId = {};

    btnLoadPosts.addEventListener('click', loadPosts);
    async function loadPosts(){
        let response = await fetch(`${BASE_URL}posts`);
        let data = await response.json();
        for (const [postId, value] of Object.entries(data)) {
            postsWithId[postId] = value.body;
            
            let newOption = document.createElement('option');
            newOption.value = postId;
            newOption.textContent = value.title;
            posts.appendChild(newOption); 
        };
    };

    btnViewPost.addEventListener('click', loadComments);
    async function loadComments(){
        commentsContainer.innerHTML = '';
        let response = await fetch(`${BASE_URL}comments`);
        let data = await response.json();

        let currentPostValue = posts.value;
        let currentPostText = posts.options[posts.selectedIndex].text;

        postTitle.textContent = currentPostText;
        postBody.textContent = postsWithId[currentPostValue]
        for (const info of Object.values(data)) {
            if (info.postId === currentPostValue){
                let newLi = document.createElement('li');
                newLi.setAttribute('id', info.id);
                newLi.textContent = info.text;
                commentsContainer.appendChild(newLi);
            };
        };
    }
}

attachEvents();