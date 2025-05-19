import sys
import os

# Add the root project directory (where `database/` lives) to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.users import Users

def test_db():
    db = Users()
    user = db.get_user_by_id(1)
    print(user)

test_db()
