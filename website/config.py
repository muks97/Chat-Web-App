from dotenv import load_dotenv
from pathlib import Path  # python3 only
import os
import sys
# set path to env file
env_path = Path('/Users/mukeshvishwanathan/Desktop/Chat-Web-App') / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    """Set Flask configuration vars from .env file."""

    # Load in enviornemnt variables
    TESTING = os.getenv('False')
    FLASK_DEBUG = os.getenv('True')
    SECRET_KEY = os.getenv('youwontguessthiskey')
    SERVER = os.getenv('0.0.0.0')
