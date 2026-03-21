"""
Th7media - Personal Brand Website
A Flask-based portfolio and learning hub for Python, Web Dev, and Design.
Author: Th7media
"""

from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'th7media-dev-key-2024')
app.config['ENV'] = os.environ.get('FLASK_ENV', 'development')
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', '1') == '1'

# Security headers for production
@app.after_request
def add_security_headers(response):
    """Add security headers for production."""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

# ==================== DATA STORE ====================

# Learning Lab Content - Easily expandable
LEARNING_TRACKS = {
    "python": {
        "title": "Python Mastery",
        "description": "From basics to advanced Python programming",
        "icon": "🐍",
        "color": "#3776ab",
        "lessons": [
            {
                "id": "py-001",
                "title": "Python Basics",
                "description": "Variables, data types, and basic operations",
                "difficulty": "Beginner",
                "duration": "30 min",
                "code_snippet": """# Variables and Data Types
name = "Th7media"
age = 25
is_developer = True

# Basic Operations
print(f"Hello, I'm {name}")
print(f"Next year I'll be {age + 1}")

# Lists
skills = ["Python", "Flask", "Design"]
print(f"My skills: {', '.join(skills)}")"""
            },
            {
                "id": "py-002",
                "title": "Control Flow",
                "description": "If statements, loops, and logic",
                "difficulty": "Beginner",
                "duration": "45 min",
                "code_snippet": """# If Statements
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

# For Loops
for i in range(5):
    print(f"Iteration {i}")

# List Comprehension
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]"""
            },
            {
                "id": "py-003",
                "title": "Functions & Modules",
                "description": "Creating reusable code blocks",
                "difficulty": "Intermediate",
                "duration": "60 min",
                "code_snippet": """# Function Definition
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Lambda Functions
multiply = lambda x, y: x * y

# Decorators
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time: {time.time() - start:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "Done!"
"""
            },
            {
                "id": "py-004",
                "title": "Object-Oriented Programming",
                "description": "Classes, objects, and inheritance",
                "difficulty": "Intermediate",
                "duration": "75 min",
                "code_snippet": """class Developer:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.experience = 0
    
    def add_skill(self, skill):
        self.skills.append(skill)
    
    def code(self):
        return f"{self.name} is coding..."

class FullStackDev(Developer):
    def __init__(self, name, skills, frontend_stack):
        super().__init__(name, skills)
        self.frontend_stack = frontend_stack
    
    def build_app(self):
        return f"Building full-stack app with {self.frontend_stack}"

# Usage
th7 = FullStackDev("Th7", ["Python"], "React")
print(th7.build_app())"""
            }
        ]
    },
    "html-css": {
        "title": "HTML5 & CSS3",
        "description": "Build beautiful, responsive web interfaces",
        "icon": "🎨",
        "color": "#e34c26",
        "lessons": [
            {
                "id": "html-001",
                "title": "HTML Structure",
                "description": "Semantic HTML and document structure",
                "difficulty": "Beginner",
                "duration": "25 min",
                "code_snippet": """<!-- Semantic HTML5 Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
</head>
<body>
    <header>
        <nav>
            <a href="#home">Home</a>
            <a href="#about">About</a>
        </nav>
    </header>
    
    <main>
        <section id="hero">
            <h1>Welcome to Th7media</h1>
            <p>Developer. Designer. Educator.</p>
        </section>
        
        <article>
            <h2>Latest Project</h2>
            <p>Building amazing web experiences...</p>
        </article>
    </main>
    
    <footer>
        <p>&copy; 2024 Th7media</p>
    </footer>
</body>
</html>"""
            },
            {
                "id": "css-001",
                "title": "CSS Flexbox",
                "description": "Modern layout with Flexbox",
                "difficulty": "Beginner",
                "duration": "40 min",
                "code_snippet": """/* Flexbox Container */
.container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    padding: 2rem;
}

/* Flex Items */
.item {
    flex: 1;
    min-width: 200px;
}

.item-featured {
    flex: 2;
    order: -1;
}

/* Centering with Flexbox */
.center-everything {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}"""
            },
            {
                "id": "css-002",
                "title": "CSS Grid",
                "description": "Two-dimensional layouts made easy",
                "difficulty": "Intermediate",
                "duration": "50 min",
                "code_snippet": """/* CSS Grid Layout */
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    grid-template-rows: auto 1fr auto;
    gap: 20px;
    padding: 2rem;
}

/* Named Grid Areas */
.layout {
    display: grid;
    grid-template-areas:
        "header header header"
        "sidebar main main"
        "footer footer footer";
    grid-template-columns: 250px 1fr 1fr;
    min-height: 100vh;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.footer { grid-area: footer; }"""
            },
            {
                "id": "css-003",
                "title": "Animations & Transitions",
                "description": "Bring your designs to life",
                "difficulty": "Intermediate",
                "duration": "45 min",
                "code_snippet": """/* Smooth Transitions */
.button {
    background: #333;
    color: white;
    padding: 12px 24px;
    transition: all 0.3s ease;
}

.button:hover {
    background: #555;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

/* Keyframe Animations */
@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-100px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.animated-element {
    animation: slideIn 0.6s ease-out forwards;
}

/* Pulse Animation */
@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}

.pulse {
    animation: pulse 2s infinite;
}"""
            }
        ]
    },
    "javascript": {
        "title": "JavaScript Essentials",
        "description": "Interactive web development with vanilla JS",
        "icon": "⚡",
        "color": "#f7df1e",
        "lessons": [
            {
                "id": "js-001",
                "title": "JS Fundamentals",
                "description": "Variables, functions, and DOM basics",
                "difficulty": "Beginner",
                "duration": "40 min",
                "code_snippet": """// Modern JavaScript (ES6+)
const name = 'Th7media';
let count = 0;

// Arrow Functions
const greet = (name) => `Hello, ${name}!`;

// Template Literals
const message = `Welcome, ${name}! 
You have ${count} notifications.`;

// DOM Manipulation
document.addEventListener('DOMContentLoaded', () => {
    const button = document.querySelector('#myButton');
    const output = document.querySelector('#output');
    
    button.addEventListener('click', () => {
        count++;
        output.textContent = `Clicked ${count} times!`;
        output.classList.add('highlight');
    });
});

// Array Methods
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);
const evens = numbers.filter(n => n % 2 === 0);"""
            },
            {
                "id": "js-002",
                "title": "Async JavaScript",
                "description": "Promises, async/await, and API calls",
                "difficulty": "Intermediate",
                "duration": "55 min",
                "code_snippet": """// Promises
const fetchData = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('Data loaded!');
        }, 1000);
    });
};

// Async/Await
async function loadUserData() {
    try {
        const response = await fetch('/api/user');
        const user = await response.json();
        console.log(user);
        return user;
    } catch (error) {
        console.error('Error:', error);
    }
}

// Fetch API
async function getGitHubRepos(username) {
    const url = `https://api.github.com/users/${username}/repos`;
    
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error('Failed to fetch');
        const repos = await response.json();
        return repos;
    } catch (error) {
        console.error('Error fetching repos:', error);
        return [];
    }
}"""
            },
            {
                "id": "js-003",
                "title": "Event Handling",
                "description": "Master user interactions",
                "difficulty": "Intermediate",
                "duration": "45 min",
                "code_snippet": """// Event Listeners
document.addEventListener('DOMContentLoaded', () => {
    
    // Click Events
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(btn => {
        btn.addEventListener('click', handleClick);
    });
    
    // Form Submission
    const form = document.querySelector('#contactForm');
    form.addEventListener('submit', handleSubmit);
    
    // Keyboard Events
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeModal();
        }
    });
    
    // Scroll Events (with debouncing)
    let scrollTimeout;
    window.addEventListener('scroll', () => {
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(() => {
            updateNavbar();
        }, 100);
    });
});

function handleClick(e) {
    e.preventDefault();
    const target = e.target;
    target.classList.toggle('active');
}"""
            },
            {
                "id": "js-004",
                "title": "Local Storage & State",
                "description": "Persist data in the browser",
                "difficulty": "Intermediate",
                "duration": "35 min",
                "code_snippet": """// Local Storage Utilities
const Storage = {
    set(key, value) {
        try {
            localStorage.setItem(key, JSON.stringify(value));
        } catch (e) {
            console.error('Storage error:', e);
        }
    },
    
    get(key) {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : null;
        } catch (e) {
            console.error('Storage error:', e);
            return null;
        }
    },
    
    remove(key) {
        localStorage.removeItem(key);
    }
};

// Progress Tracker Example
class ProgressTracker {
    constructor() {
        this.progress = Storage.get('learningProgress') || {};
    }
    
    completeLesson(lessonId) {
        this.progress[lessonId] = {
            completed: true,
            completedAt: new Date().toISOString()
        };
        this.save();
    }
    
    save() {
        Storage.set('learningProgress', this.progress);
    }
    
    getCompletionRate(totalLessons) {
        const completed = Object.keys(this.progress).length;
        return Math.round((completed / totalLessons) * 100);
    }
}"""
            }
        ]
    }
}

# Portfolio Projects
PROJECTS = [
    {
        "id": 1,
        "title": "Zimhub",
        "category": "Web Development",
        "description": "A community platform connecting developers and creators in Zimbabwe. Features real-time chat, project collaboration, and resource sharing.",
        "technologies": ["Python", "Flask", "Socket.IO", "PostgreSQL"],
        "image": "zimhub.jpg",
        "link": "#",
        "github": "#"
    },
    {
        "id": 2,
        "title": "E-Learning Dashboard",
        "category": "Web Development",
        "description": "Interactive learning management system with progress tracking, quizzes, and video content delivery.",
        "technologies": ["JavaScript", "Node.js", "MongoDB", "React"],
        "image": "elearning.jpg",
        "link": "#",
        "github": "#"
    },
    {
        "id": 3,
        "title": "Brand Identity System",
        "category": "Graphic Design",
        "description": "Complete brand identity including logo design, color palette, typography guidelines, and marketing materials.",
        "technologies": ["Figma", "Adobe Illustrator", "Photoshop"],
        "image": "branding.jpg",
        "link": "#",
        "github": None
    },
    {
        "id": 4,
        "title": "Portfolio Generator",
        "category": "Web Development",
        "description": "Tool for developers to quickly generate professional portfolio websites from GitHub profiles.",
        "technologies": ["Python", "Jinja2", "GitHub API", "Tailwind"],
        "image": "portfolio.jpg",
        "link": "#",
        "github": "#"
    },
    {
        "id": 5,
        "title": "Mobile App UI Kit",
        "category": "Graphic Design",
        "description": "Comprehensive UI kit with 50+ screens for fintech mobile applications.",
        "technologies": ["Figma", "Auto Layout", "Components"],
        "image": "uikit.jpg",
        "link": "#",
        "github": None
    },
    {
        "id": 6,
        "title": "Code Snippet Manager",
        "category": "Web Development",
        "description": "Browser extension for saving, organizing, and sharing code snippets across devices.",
        "technologies": ["JavaScript", "Chrome API", "Firebase"],
        "image": "snippet.jpg",
        "link": "#",
        "github": "#"
    }
]

# Skills Data
SKILLS = {
    "languages": ["Python", "JavaScript", "HTML5", "CSS3", "SQL"],
    "frameworks": ["Flask", "Django", "React", "Node.js", "Express"],
    "tools": ["Git", "Docker", "Figma", "VS Code", "Linux"],
    "design": ["UI/UX Design", "Brand Identity", "Typography", "Color Theory"]
}

# ==================== ROUTES ====================

@app.route('/')
def home():
    """Home page with hero section and featured content."""
    featured_projects = PROJECTS[:3]
    return render_template('index.html', 
                         projects=featured_projects,
                         skills=SKILLS,
                         tracks=LEARNING_TRACKS)

@app.route('/portfolio')
def portfolio():
    """Full portfolio page with all projects."""
    category = request.args.get('category', 'all')
    
    if category == 'all':
        filtered_projects = PROJECTS
    else:
        filtered_projects = [p for p in PROJECTS if p['category'].lower().replace(' ', '-') == category]
    
    return render_template('portfolio.html', 
                         projects=filtered_projects,
                         active_category=category)

@app.route('/learning-lab')
def learning_lab():
    """Learning Lab main page with all tracks."""
    track_id = request.args.get('track')
    
    if track_id and track_id in LEARNING_TRACKS:
        track = LEARNING_TRACKS[track_id]
        return render_template('track_detail.html', 
                             track=track,
                             track_id=track_id,
                             all_tracks=LEARNING_TRACKS)
    
    # Calculate total lessons for progress tracking
    total_lessons = sum(len(t['lessons']) for t in LEARNING_TRACKS.values())
    
    return render_template('learning_lab.html',
                         tracks=LEARNING_TRACKS,
                         total_lessons=total_lessons)

@app.route('/api/lesson/<lesson_id>')
def get_lesson(lesson_id):
    """API endpoint to get lesson details."""
    for track_id, track in LEARNING_TRACKS.items():
        for lesson in track['lessons']:
            if lesson['id'] == lesson_id:
                return jsonify({
                    'success': True,
                    'lesson': lesson,
                    'track': track_id
                })
    return jsonify({'success': False, 'error': 'Lesson not found'}), 404

@app.route('/api/progress', methods=['GET', 'POST'])
def progress():
    """Handle progress tracking (frontend storage with backend validation)."""
    if request.method == 'POST':
        data = request.get_json()
        # In production, this would save to database
        return jsonify({
            'success': True,
            'message': 'Progress saved',
            'data': data
        })
    
    # GET request - return sample progress structure
    return jsonify({
        'success': True,
        'progress': {}
    })

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact form for freelance/tutoring inquiries."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        inquiry_type = request.form.get('inquiry_type')
        
        # Validation
        if not all([name, email, subject, message]):
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'success': False, 'error': 'Please fill all fields'})
            flash('Please fill all required fields.', 'error')
            return redirect(url_for('contact'))
        
        # In production, send email or save to database
        # For now, just return success
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({
                'success': True,
                'message': 'Thank you! Your message has been sent successfully.'
            })
        
        flash('Thank you! Your message has been sent successfully.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/about')
def about():
    """About page with bio and experience."""
    return render_template('about.html', skills=SKILLS)

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500

# ==================== CONTEXT PROCESSORS ====================

@app.context_processor
def inject_globals():
    """Make global data available to all templates."""
    return {
        'current_year': datetime.now().year,
        'site_name': 'Th7media',
        'tagline': 'Developer. Designer. Educator.',
        'social_links': {
            'github': 'https://github.com/th7media',
            'linkedin': 'https://linkedin.com/in/th7media',
            'twitter': 'https://twitter.com/th7media',
            'dribbble': 'https://dribbble.com/th7media'
        }
    }

# ==================== MAIN ====================

if __name__ == '__main__':
    # Use PORT from environment (Render sets this) or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
