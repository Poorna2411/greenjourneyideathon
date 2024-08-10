document.addEventListener('DOMContentLoaded', function() {
    const posts = document.querySelectorAll('.blog-post');
    posts.forEach(post => {
        post.addEventListener('click', () => {
            alert(`You clicked on ${post.querySelector('h2').innerText}`);
        });
    });
});
