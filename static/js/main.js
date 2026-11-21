/**
 * CineSet - Main JavaScript
 * Common utilities and functions used across the application
 */

// CSRF Token helper for Django
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// API fetch helper with CSRF token
async function apiFetch(url, options = {}) {
    const defaultOptions = {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        credentials: 'same-origin',
    };
    
    const mergedOptions = {
        ...defaultOptions,
        ...options,
        headers: {
            ...defaultOptions.headers,
            ...options.headers,
        },
    };
    
    const response = await fetch(url, mergedOptions);
    
    if (!response.ok) {
        const error = await response.json().catch(() => ({ error: 'Request failed' }));
        throw new Error(error.error || `HTTP ${response.status}`);
    }
    
    return response.json();
}

// Show loading spinner
function showLoading(element) {
    element.innerHTML = `
        <div class="spinner"></div>
        <p class="loading-text">Loading...</p>
    `;
}

// Show error message
function showError(element, message) {
    element.innerHTML = `
        <div class="alert alert-error">
            <strong>Error:</strong> ${message}
        </div>
    `;
}

// Show success message
function showSuccess(element, message) {
    element.innerHTML = `
        <div class="alert alert-success">
            ${message}
        </div>
    `;
}

// Format Jaccard similarity as percentage
function formatSimilarity(score) {
    return `${(score * 100).toFixed(1)}%`;
}

// Create movie card HTML
function createMovieCard(movie, similarity = null, matchingGenres = null) {
    const genres = Array.isArray(movie.genres) 
        ? movie.genres 
        : (typeof movie.genres === 'string' ? movie.genres.split(',') : []);
    
    const genreTags = genres.map(genre => 
        `<span class="genre-tag">${genre.trim()}</span>`
    ).join('');
    
    const ratingHtml = movie.average_rating 
        ? `<div class="movie-rating">⭐ ${movie.average_rating}/10</div>` 
        : '';
    
    const similarityHtml = similarity !== null 
        ? `<div class="movie-rating" style="color: var(--secondary-color);">
             📊 ${formatSimilarity(similarity)} match
           </div>` 
        : '';
    
    const matchingHtml = matchingGenres && matchingGenres.length > 0
        ? `<div style="margin-top: var(--spacing-xs); font-size: 0.875rem; color: var(--success-color);">
             ✓ Matches: ${matchingGenres.join(', ')}
           </div>`
        : '';
    
    return `
        <div class="movie-card">
            <div class="movie-poster" style="background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%); display: flex; align-items: center; justify-content: center; color: var(--text-muted);">
                🎬
            </div>
            <div class="movie-info">
                <div class="movie-title" title="${movie.title}">${movie.title}</div>
                ${movie.release_year ? `<div class="movie-year">${movie.release_year}</div>` : ''}
                <div class="movie-genres">${genreTags}</div>
                ${ratingHtml}
                ${similarityHtml}
                ${matchingHtml}
            </div>
        </div>
    `;
}

// Create genre checkbox HTML
function createGenreCheckbox(genre, name, checked = false) {
    return `
        <div class="form-check">
            <input 
                type="checkbox" 
                id="${name}_${genre.id}" 
                name="${name}" 
                value="${genre.id}" 
                class="form-check-input"
                ${checked ? 'checked' : ''}
            >
            <label for="${name}_${genre.id}" class="form-label" style="margin-bottom: 0; cursor: pointer;">
                ${genre.name}
            </label>
        </div>
    `;
}

// Debounce function for search inputs
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Auto-hide alerts after 5 seconds
document.addEventListener('DOMContentLoaded', () => {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.5s ease';
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
});

// Export for use in other scripts
window.CineSet = {
    apiFetch,
    showLoading,
    showError,
    showSuccess,
    formatSimilarity,
    createMovieCard,
    createGenreCheckbox,
    debounce,
    getCookie,
    csrftoken,
};
