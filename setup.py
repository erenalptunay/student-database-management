# setup.py

from models import setup_database
from operations import load_lessons, load_departments


setup_database()
load_departments()
load_lessons()
