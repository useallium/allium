from database.base import Database
from werkzeug.security import generate_password_hash, check_password_hash

class Users(Database):

    def get_all_users(self):
        """
        Retrieve all users in database
        """
        query = "SELECT * FROM Users"
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        return users
    
    def get_user_by_id(self, user_id):
        """
        Retrieve specific user given their user_id
        """
        query = "SELECT * FROM Users WHERE user_id = %s"
        self.cursor.execute(query, (user_id,))
        user = self.cursor.fetchone()
        return user

    def update_user(self, user_id, email, first_name, last_name, user_type, profile_picture):
        """
        Update a user's information in the database given their user_id.
        """
        query = """
            UPDATE Users
            SET email = %s,
                first_name = %s,
                last_name = %s,
                user_type = %s,
                profile_picture = %s
            WHERE user_id = %s
        """
        self.cursor.execute(query, (email, first_name, last_name, user_type, profile_picture, user_id))
        self.conn.commit()
        return self.cursor.rowcount
    

    def change_password(self, user_id, new_password):
        query="""
            Update Users
            SET password_hash = %s
            WHERE user_id = %s
        """
        password_hashed = generate_password_hash(new_password)
        self.cursor.execute(query, (password_hashed, user_id))
        self.conn.commit()
        return self.cursor.rowcount
    
        

    def add_user(self, email, first_name, last_name, password_hash, user_type):
        query = "INSERT INTO Users (email, first_name, last_name, password_hash, user_type) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(query,(email,first_name,last_name,password_hash,user_type))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_user_by_email(self, email):
        query = "SELECT user_id, email, password_hash, user_type FROM Users WHERE email = %s"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchone()

        if result:
            return {
                'user_id': result['user_id'],
                'email': result['email'],
                'password_hash': result['password_hash'],
                'user_type': result['user_type']
            }
        return None

