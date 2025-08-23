document.addEventListener('DOMContentLoaded', function() {
    console.log('Blog page loaded');

    // Example: highlight the first heading
    const heading = document.querySelector('h2');
    if (heading) {
        heading.style.color = '#2c7be5'; // change heading color
    }

    // Example: show a welcome alert on the register page
    if (document.body.classList.contains('register-page')) {
        alert('Welcome! Please fill in your details to register.');
    }
});