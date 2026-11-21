// Movie Explorer JavaScript - Enhanced

document.addEventListener('DOMContentLoaded', function () {
    console.log('Movie Explorer Initialized');

    // Smooth scroll to movies grid
    const filtersForm = document.getElementById('filtersForm');
    if (filtersForm) {
        filtersForm.addEventListener('submit', function (e) {
            // Let form submit naturally, just add visual feedback
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.innerHTML = '<span>Loading...</span><span class="btn-icon">⏳</span>';
                submitBtn.disabled = true;
            }
        });
    }

    // Add loading state to favorite buttons
    const favoriteForms = document.querySelectorAll('.favorite-form');
    favoriteForms.forEach(form => {
        form.addEventListener('submit', function (e) {
            const button = this.querySelector('.btn-favorite');
            if (button) {
                button.style.transform = 'scale(1.3) rotate(360deg)';
                button.style.transition = 'transform 0.5s ease';
            }
        });
    });

    // Intersection Observer for fade-in animation
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe all movie cards
    const movieCards = document.querySelectorAll('.movie-card');
    movieCards.forEach(card => {
        observer.observe(card);
    });

    // Add ripple effect to buttons
    function createRipple(event) {
        const button = event.currentTarget;
        const ripple = document.createElement('span');
        const rect = button.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = event.clientX - rect.left - size / 2;
        const y = event.clientY - rect.top - size / 2;

        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.classList.add('ripple');

        button.appendChild(ripple);

        setTimeout(() => {
            ripple.remove();
        }, 600);
    }

    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', createRipple);
    });

    // Enhanced search input with visual feedback
    const searchInput = document.querySelector('input[name="search"]');
    if (searchInput) {
        searchInput.addEventListener('focus', function () {
            this.parentElement.style.transform = 'scale(1.02)';
            this.parentElement.style.transition = 'transform 0.3s ease';
        });

        searchInput.addEventListener('blur', function () {
            this.parentElement.style.transform = 'scale(1)';
        });

        // Search suggestions or highlighting (future enhancement)
        let searchTimeout;
        searchInput.addEventListener('input', function () {
            clearTimeout(searchTimeout);
            const value = this.value.trim();

            if (value.length > 0) {
                this.style.borderColor = 'var(--success)';
            } else {
                this.style.borderColor = '#E0E0E0';
            }
        });
    }

    // Add hover sound effect (optional - subtle)
    const movieCardsForSound = document.querySelectorAll('.movie-card');
    movieCardsForSound.forEach(card => {
        card.addEventListener('mouseenter', function () {
            // Visual feedback on hover
            this.style.zIndex = '10';
        });

        card.addEventListener('mouseleave', function () {
            this.style.zIndex = '1';
        });
    });

    // Stats counter animation
    function animateCounter(element, target) {
        let current = 0;
        const increment = target / 50;
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                element.textContent = target;
                clearInterval(timer);
            } else {
                element.textContent = Math.ceil(current);
            }
        }, 20);
    }

    // Animate stat values on page load
    const statValues = document.querySelectorAll('.stat-value');
    statValues.forEach(stat => {
        const targetValue = parseFloat(stat.textContent);
        if (!isNaN(targetValue)) {
            stat.textContent = '0';
            setTimeout(() => {
                animateCounter(stat, targetValue);
            }, 300);
        }
    });

    // Smooth scroll to results when filters applied
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.toString()) {
        setTimeout(() => {
            const moviesGrid = document.querySelector('.movies-grid');
            if (moviesGrid) {
                moviesGrid.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }, 100);
    }

    // Add parallax effect to hero section
    window.addEventListener('scroll', function () {
        const heroSection = document.querySelector('.explorer-hero');
        if (heroSection) {
            const scrolled = window.pageYOffset;
            heroSection.style.transform = `translateY(${scrolled * 0.3}px)`;
            heroSection.style.opacity = 1 - (scrolled / 500);
        }
    });

    // Filter chips animation
    const filterInputs = document.querySelectorAll('.filter-input, .filter-select');
    filterInputs.forEach(input => {
        input.addEventListener('change', function () {
            this.style.borderColor = 'var(--primary)';
            setTimeout(() => {
                this.style.borderColor = '#E0E0E0';
            }, 1000);
        });
    });

    // Add active filter indicator
    const activeFilters = [];
    const genreSelect = document.querySelector('select[name="genre"]');
    const yearSelect = document.querySelector('select[name="year"]');
    const ratingSelect = document.querySelector('select[name="rating"]');
    const languageSelect = document.querySelector('select[name="language"]');

    function updateActiveFilters() {
        const indicators = document.querySelector('.active-filters-container');
        // Could add visual indicators for active filters
    }

    // Genre tags hover effect enhancement
    const genreTags = document.querySelectorAll('.genre-tag');
    genreTags.forEach(tag => {
        tag.addEventListener('mouseenter', function () {
            // Could trigger genre filtering or highlighting
        });
    });

    console.log(`Loaded ${movieCards.length} movie cards`);
});

// Add CSS for ripple effect dynamically
const style = document.createElement('style');
style.textContent = `
    .btn {
        position: relative;
        overflow: hidden;
    }
    
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.6);
        transform: scale(0);
        animation: ripple-animation 0.6s ease-out;
        pointer-events: none;
    }
    
    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
