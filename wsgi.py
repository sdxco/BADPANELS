"""
WSGI entry point for gunicorn
"""
import sys
import os

# Add the application root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and expose the Flask app
from acoustic_fella.web.app import app

if __name__ == "__main__":
    app.run()
