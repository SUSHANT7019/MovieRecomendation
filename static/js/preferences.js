// Preferences page JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    
    // Add animation when checking/unchecking
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const label = this.nextElementSibling;
            if (this.checked) {
                label.style.animation = 'pulse 0.3s ease';
            }
            setTimeout(() => {
                label.style.animation = '';
            }, 300);
        });
    });
    
    // Form validation
    const form = document.querySelector('.preferences-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const checkedBoxes = document.querySelectorAll('input[type="checkbox"]:checked');
            if (checkedBoxes.length === 0) {
                e.preventDefault();
                showNotification('Please select at least one genre', 'warning');
            }
        });
    }
});
