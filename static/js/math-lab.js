// Math Lab JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Add interactivity to the math lab
    const form = document.querySelector('.lab-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const setA = document.getElementById('set_a').value.trim();
            const setB = document.getElementById('set_b').value.trim();
            
            if (!setA && !setB) {
                e.preventDefault();
                showNotification('Please enter at least one set', 'warning');
            }
        });
    }
    
    // Animate results on load
    const resultCards = document.querySelectorAll('.result-card');
    resultCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        setTimeout(() => {
            card.style.transition = 'all 0.5s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
});
