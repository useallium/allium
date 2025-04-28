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
