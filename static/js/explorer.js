document.addEventListener('DOMContentLoaded', function() {
    // Handle favorite/unfavorite with AJAX
    document.querySelectorAll('.favorite-form').forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const button = this.querySelector('.btn-favorite');
            const movieCard = this.closest('.movie-card');
            const favoriteBadge = movieCard.querySelector('.favorite-badge');
            
            // Add loading state
            button.classList.add('loading');
            
            // Get CSRF token
            const csrfToken = this.querySelector('[name=csrfmiddlewaretoken]').value;
            
            // Make AJAX request
            fetch(this.action, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                credentials: 'same-origin'
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    if (data.action === 'added') {
                        // Update button to "remove" state
                        button.textContent = '♥';
                        button.classList.add('favorited');
                        button.title = 'Remove from favorites';
                        this.action = this.action.replace('/add/', '/remove/');
                        
                        // Add favorite badge
                        if (!favoriteBadge) {
                            const badge = document.createElement('div');
                            badge.className = 'favorite-badge';
                            badge.textContent = '♥ Favorite';
                            movieCard.querySelector('.movie-poster-wrapper').appendChild(badge);
                        }
                    } else {
                        // Update button to "add" state
                        button.textContent = '♡';
                        button.classList.remove('favorited');
                        button.title = 'Add to favorites';
                        this.action = this.action.replace('/remove/', '/add/');
                        
                        // Remove favorite badge
                        if (favoriteBadge) {
                            favoriteBadge.remove();
                        }
                    }
                }
                button.classList.remove('loading');
            })
            .catch(error => {
                console.error('Error:', error);
                button.classList.remove('loading');
                alert('An error occurred. Please try again.');
            });
        });
    });
});
