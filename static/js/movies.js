// Movie explorer JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Auto-submit form on filter change (optional, can be removed if not desired)
    const filterSelects = document.querySelectorAll('.filter-select');
    filterSelects.forEach(select => {
        select.addEventListener('change', function() {
            // Optionally auto-submit the form
            // this.form.submit();
        });
    });
    
    // Search input with delay
    const searchInput = document.querySelector('input[name="search"]');
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            // Optionally implement auto-search with delay
        });
    }
});
