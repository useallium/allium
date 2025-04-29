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

    def update_user(self, user_id, name, email, phone, address):
        """
        Update a user's information in the database given their user_id.
        """
        query = """
            UPDATE Users
            SET name = %s,
                email = %s,
                phone = %s,
                address = %s
            WHERE user_id = %s
        """
        self.cursor.execute(query, (name, email, phone, address, user_id))
        self.conn.commit()  # Commit the changes to the database
        return self.cursor.rowcount  # Returns the number of rows updated (1 if successful, 0 if no change)
