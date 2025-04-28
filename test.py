from db import connect

def test_db():
    conn = connect()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Users")
    user = cursor.fetchone()

    print(user)

test_db()