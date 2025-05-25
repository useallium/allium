import sys
import os

# Add the root project directory (where `database/` lives) to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import date
from database.students import Students
from database.internships import Internships

