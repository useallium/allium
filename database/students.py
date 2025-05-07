from database.base import Database

class Students(Database):
    def get_students(self):
        query = "SELECT * FROM Students"
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        return users
    