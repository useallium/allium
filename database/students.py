from database.base import Database

class Students(Database):
    def get_students(self):
        query = "SELECT * FROM Students"
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        return users
    
    def get_student_by_id(self,student_id):
        query = "SELECT * FROM Students WHERE student_id = %s"
        self.cursor.execute(query,(student_id))
        user = self.cursor.fetchone()
        return user
    