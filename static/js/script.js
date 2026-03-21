/**
 * Th7media - Main JavaScript
 * Handles navigation, scroll effects, and UI interactions
 */

document.addEventListener('DOMContentLoaded', () => {
    // Initialize all modules
    initNavigation();
    initScrollEffects();
    initScrollToTop();
    initSmoothScroll();
    initAnimations();
});

// ========================================
// NAVIGATION
// ========================================

function initNavigation() {
    const navbar = document.getElementById('navbar');
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    
    // Navbar scroll effect
    let lastScroll = 0;
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        // Add/remove scrolled class
        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        // Hide/show navbar on scroll (optional)
        if (currentScroll > lastScroll && currentScroll > 100) {
            navbar.style.transform = 'translateY(-100%)';
        } else {
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScroll = currentScroll;
    });
    
    // Mobile menu toggle
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            navToggle.classList.toggle('active');
            
            // Animate hamburger
            const hamburgers = navToggle.querySelectorAll('.hamburger');
            if (navToggle.classList.contains('active')) {
                hamburgers[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
                hamburgers[1].style.opacity = '0';
                hamburgers[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
            } else {
                hamburgers[0].style.transform = 'none';
                hamburgers[1].style.opacity = '1';
                hamburgers[2].style.transform = 'none';
            }
        });
        
        // Close menu on link click
        const navLinks = navMenu.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                navToggle.classList.remove('active');
                const hamburgers = navToggle.querySelectorAll('.hamburger');
                hamburgers[0].style.transform = 'none';
                hamburgers[1].style.opacity = '1';
                hamburgers[2].style.transform = 'none';
            });
        });
    }
}

// ========================================
// SCROLL EFFECTS
// ========================================

function initScrollEffects() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements with animation classes
    const animateElements = document.querySelectorAll(
        '.skill-card, .project-card, .track-card-large, .tip-card, .lesson-card, .process-step, .faq-item'
    );
    
    animateElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = `opacity 0.5s ease ${index * 0.05}s, transform 0.5s ease ${index * 0.05}s`;
        observer.observe(el);
    });
}

// Add CSS class for animated elements
const style = document.createElement('style');
style.textContent = `
    .animate-in {
        opacity: 1 !important;
        transform: translateY(0) !important;
    }
`;
document.head.appendChild(style);

// ========================================
// SCROLL TO TOP
// ========================================

function initScrollToTop() {
    const scrollTopBtn = document.getElementById('scrollTop');
    
    if (!scrollTopBtn) return;
    
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 500) {
            scrollTopBtn.classList.add('visible');
        } else {
            scrollTopBtn.classList.remove('visible');
        }
    });
    
    scrollTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// ========================================
// SMOOTH SCROLL
// ========================================

function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const navHeight = document.getElementById('navbar')?.offsetHeight || 70;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ========================================
// ANIMATIONS
// ========================================

function initAnimations() {
    // Parallax effect for hero orbs
    const orbs = document.querySelectorAll('.gradient-orb');
    
    if (orbs.length && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            
            orbs.forEach((orb, index) => {
                const speed = 0.1 + (index * 0.05);
                orb.style.transform = `translateY(${scrolled * speed}px)`;
            });
        });
    }
    
    // Counter animation for stats
    animateCounters();
}

function animateCounters() {
    const counters = document.querySelectorAll('.stat-number, .progress-value');
    
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const text = counter.textContent;
                const numMatch = text.match(/[\d.]+/);
                
                if (numMatch) {
                    const targetNum = parseFloat(numMatch[0]);
                    const suffix = text.replace(/[\d.]+/, '');
                    const duration = 2000;
                    const startTime = performance.now();
                    
                    const animate = (currentTime) => {
                        const elapsed = currentTime - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        
                        // Easing function
                        const easeOutQuart = 1 - Math.pow(1 - progress, 4);
                        const currentNum = Math.floor(targetNum * easeOutQuart);
                        
                        counter.textContent = currentNum + suffix;
                        
                        if (progress < 1) {
                            requestAnimationFrame(animate);
                        } else {
                            counter.textContent = targetNum + suffix;
                        }
                    };
                    
                    requestAnimationFrame(animate);
                }
                
                counterObserver.unobserve(counter);
            }
        });
    }, { threshold: 0.5 });
    
    counters.forEach(counter => counterObserver.observe(counter));
}

// ========================================
// UTILITY FUNCTIONS
// ========================================

// Debounce function
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

// Throttle function
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Check if element is in viewport
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// ========================================
// CODE SNIPPET UTILITIES
// ========================================

const CodeUtils = {
    // Copy code to clipboard
    async copyToClipboard(text) {
        try {
            await navigator.clipboard.writeText(text);
            return true;
        } catch (err) {
            console.error('Failed to copy:', err);
            return false;
        }
    },
    
    // Syntax highlighting (basic)
    highlightCode(code, language) {
        // This is a simple placeholder - in production, use Prism.js or highlight.js
        const keywords = {
            python: ['def', 'class', 'return', 'if', 'else', 'elif', 'for', 'while', 'try', 'except', 'import', 'from', 'as', 'lambda', 'yield'],
            javascript: ['function', 'const', 'let', 'var', 'return', 'if', 'else', 'for', 'while', 'try', 'catch', 'async', 'await', 'import', 'export', 'class'],
            css: ['display', 'position', 'color', 'background', 'margin', 'padding', 'width', 'height', 'flex', 'grid']
        };
        
        let highlighted = code;
        const langKeywords = keywords[language] || [];
        
        langKeywords.forEach(keyword => {
            const regex = new RegExp(`\\b${keyword}\\b`, 'g');
            highlighted = highlighted.replace(regex, `<span class="code-keyword">${keyword}</span>`);
        });
        
        return highlighted;
    }
};

// ========================================
// PROGRESS TRACKING
// ========================================

const ProgressTracker = {
    STORAGE_KEY: 'th7media_progress',
    
    getProgress() {
        try {
            const data = localStorage.getItem(this.STORAGE_KEY);
            return data ? JSON.parse(data) : {};
        } catch (e) {
            console.error('Error reading progress:', e);
            return {};
        }
    },
    
    saveProgress(progress) {
        try {
            localStorage.setItem(this.STORAGE_KEY, JSON.stringify(progress));
        } catch (e) {
            console.error('Error saving progress:', e);
        }
    },
    
    completeLesson(lessonId) {
        const progress = this.getProgress();
        progress[lessonId] = {
            completed: true,
            completedAt: new Date().toISOString()
        };
        this.saveProgress(progress);
        return progress;
    },
    
    isCompleted(lessonId) {
        const progress = this.getProgress();
        return progress[lessonId]?.completed || false;
    },
    
    getCompletionRate(lessonIds) {
        const progress = this.getProgress();
        const completed = lessonIds.filter(id => progress[id]?.completed).length;
        return Math.round((completed / lessonIds.length) * 100);
    },
    
    reset() {
        localStorage.removeItem(this.STORAGE_KEY);
    }
};

// ========================================
// FORM UTILITIES
// ========================================

const FormUtils = {
    // Validate email
    isValidEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    },
    
    // Sanitize input
    sanitizeInput(input) {
        const div = document.createElement('div');
        div.textContent = input;
        return div.innerHTML;
    },
    
    // Show field error
    showError(field, message) {
        const formGroup = field.closest('.form-group');
        formGroup.classList.add('error');
        
        let errorEl = formGroup.querySelector('.error-message');
        if (!errorEl) {
            errorEl = document.createElement('span');
            errorEl.className = 'error-message';
            formGroup.appendChild(errorEl);
        }
        errorEl.textContent = message;
    },
    
    // Clear field error
    clearError(field) {
        const formGroup = field.closest('.form-group');
        formGroup.classList.remove('error');
        const errorEl = formGroup.querySelector('.error-message');
        if (errorEl) errorEl.remove();
    }
};

// ========================================
// NOTIFICATION SYSTEM
// ========================================

const Notifications = {
    container: null,
    
    init() {
        if (!this.container) {
            this.container = document.createElement('div');
            this.container.className = 'notification-container';
            document.body.appendChild(this.container);
            
            // Add styles
            const style = document.createElement('style');
            style.textContent = `
                .notification-container {
                    position: fixed;
                    top: 90px;
                    right: 20px;
                    z-index: 10000;
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                }
                .notification {
                    background: var(--color-bg-card);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    border-radius: 8px;
                    padding: 16px 20px;
                    min-width: 300px;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
                    animation: slideIn 0.3s ease;
                    display: flex;
                    align-items: center;
                    gap: 12px;
                }
                .notification.success { border-left: 3px solid #22c55e; }
                .notification.error { border-left: 3px solid #ef4444; }
                .notification.info { border-left: 3px solid #6366f1; }
                @keyframes slideIn {
                    from { transform: translateX(100%); opacity: 0; }
                    to { transform: translateX(0); opacity: 1; }
                }
                @keyframes slideOut {
                    from { transform: translateX(0); opacity: 1; }
                    to { transform: translateX(100%); opacity: 0; }
                }
            `;
            document.head.appendChild(style);
        }
    },
    
    show(message, type = 'info', duration = 3000) {
        this.init();
        
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.innerHTML = `
            <span>${message}</span>
        `;
        
        this.container.appendChild(notification);
        
        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease forwards';
            setTimeout(() => notification.remove(), 300);
        }, duration);
    },
    
    success(message, duration) {
        this.show(message, 'success', duration);
    },
    
    error(message, duration) {
        this.show(message, 'error', duration);
    },
    
    info(message, duration) {
        this.show(message, 'info', duration);
    }
};

// ========================================
// EXPORT FOR MODULE USE
// ========================================

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        CodeUtils,
        ProgressTracker,
        FormUtils,
        Notifications,
        debounce,
        throttle,
        isInViewport
    };
}
