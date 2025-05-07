from database.base import Database

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

    def update_user(self, user_id, email, first_name, last_name, password_hash, user_type, profile_picture):
        """
        Update a user's information in the database given their user_id.
        """
        query = """
            UPDATE Users
            SET email = %s,
                first_name = %s,
                last_name = %s,
                password_hash = %s,
                user_type = %s,
                profile_picture = %s
            WHERE user_id = %s
        """
        self.cursor.execute(query, (email, first_name, last_name, password_hash, user_type, profile_picture, user_id))
        self.conn.commit()
        return self.cursor.rowcount
    
    