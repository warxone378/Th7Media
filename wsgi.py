"""
WSGI entry point for production deployment on Render.
This file is used by Gunicorn to run the Flask application.
"""

import os
from app import app

# Ensure production settings
app.config['ENV'] = 'production'
app.config['DEBUG'] = False

# Get port from environment variable (Render sets this)
port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    # This block is only executed when running directly (not via Gunicorn)
    app.run(host='0.0.0.0', port=port)
