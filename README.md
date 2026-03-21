# Th7media - Personal Brand Website

A professional portfolio and learning hub built with Flask, featuring a minimalist dark mode design, interactive Learning Lab, and progress tracking.

![Th7media Screenshot](screenshot.png)

## Features

### Portfolio
- Hero section with dynamic typing effect
- Project showcase with filtering
- Skills & expertise display
- Responsive grid layout

### Learning Lab
- **Python Track**: From basics to OOP
- **HTML/CSS Track**: Modern layout techniques
- **JavaScript Track**: Interactive web development
- Progress tracking (localStorage-based)
- Interactive code snippets with copy functionality
- Expandable lesson cards

### Contact
- Functional contact form
- Service information
- FAQ section
- Social links

## Tech Stack

- **Backend**: Python 3.8+, Flask
- **Frontend**: HTML5, CSS3 (Flexbox/Grid), Vanilla JavaScript
- **Design**: Minimalist dark mode with accent colors
- **Fonts**: Inter, JetBrains Mono

## Project Structure

```
th7media/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── static/
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   ├── js/
│   │   └── script.js      # Main JavaScript
│   └── images/            # Static images
└── templates/
    ├── base.html          # Base template
    ├── index.html         # Home page
    ├── portfolio.html     # Portfolio page
    ├── learning_lab.html  # Learning Lab main
    ├── track_detail.html  # Individual track page
    ├── contact.html       # Contact form
    ├── about.html         # About page
    ├── 404.html           # Error page
    └── 500.html           # Error page
```

## Setup Instructions

### Option 1: Local Development (Python)

1. **Clone or download the project**
   ```bash
   cd th7media
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   Navigate to `http://localhost:5000`

### Option 2: Termux (Android)

1. **Install Termux** from F-Droid or Play Store

2. **Update packages and install Python**
   ```bash
   pkg update
   pkg install python git
   ```

3. **Clone/download the project**
   ```bash
   cd ~
   # Copy project files to ~/th7media
   cd th7media
   ```

4. **Install dependencies**
   ```bash
   pip install flask
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access locally**
   Open your device's browser and go to `http://localhost:5000`

### Option 3: Production Deployment

#### Deploy to Render (Free)

1. Create a `render.yaml` file:
   ```yaml
   services:
     - type: web
       name: th7media
       env: python
       buildCommand: pip install -r requirements.txt
       startCommand: gunicorn app:app
       envVars:
         - key: PYTHON_VERSION
           value: 3.11.0
         - key: SECRET_KEY
           generateValue: true
   ```

2. Add gunicorn to `requirements.txt`:
   ```
   gunicorn==21.2.0
   ```

3. Push to GitHub and connect to Render

#### Deploy to PythonAnywhere (Free)

1. Upload files via SFTP or Git
2. Create a new web app with Flask
3. Set the working directory
4. Reload the application

## Customization

### Adding New Lessons

Edit `app.py` and add lessons to the `LEARNING_TRACKS` dictionary:

```python
"python": {
    "title": "Python Mastery",
    "description": "...",
    "icon": "🐍",
    "color": "#3776ab",
    "lessons": [
        {
            "id": "py-005",  # Unique ID
            "title": "Your New Lesson",
            "description": "Lesson description",
            "difficulty": "Beginner",  # Beginner/Intermediate/Advanced
            "duration": "30 min",
            "code_snippet": """# Your code here"""
        }
    ]
}
```

### Adding New Projects

Add to the `PROJECTS` list in `app.py`:

```python
{
    "id": 7,
    "title": "New Project",
    "category": "Web Development",
    "description": "Project description",
    "technologies": ["Python", "Flask"],
    "image": "project.jpg",
    "link": "https://...",
    "github": "https://github.com/..."
}
```

### Changing Colors

Edit CSS variables in `static/css/style.css`:

```css
:root {
    --color-accent: #6366f1;        /* Primary accent */
    --color-accent-light: #818cf8;  /* Light accent */
    --color-accent-dark: #4f46e5;   /* Dark accent */
}
```

## Environment Variables

Create a `.env` file for production:

```env
SECRET_KEY=your-secret-key-here
FLASK_ENV=production
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/portfolio` | GET | Portfolio page |
| `/learning-lab` | GET | Learning Lab |
| `/api/lesson/<id>` | GET | Get lesson details (JSON) |
| `/api/progress` | GET/POST | Progress tracking |
| `/contact` | GET/POST | Contact form |

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Android)

## Performance

- No external JavaScript libraries
- Minimal CSS (single file)
- Optimized fonts (Google Fonts with `display=swap`)
- Lazy loading ready for images
- LocalStorage for progress (no server storage needed)

## Accessibility

- Semantic HTML5 elements
- ARIA labels
- Keyboard navigation support
- Focus indicators
- Reduced motion support
- High contrast mode support

## License

MIT License - feel free to use this template for your own portfolio!

## Credits

- Fonts: [Inter](https://rsms.me/inter/) & [JetBrains Mono](https://www.jetbrains.com/lp/mono/)
- Icons: Custom SVG
- Design: Minimalist dark mode by Th7media

---

Built with ❤️ using Flask and passion for clean code.
