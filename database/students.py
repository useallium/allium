from database.base import Database

class Students(Database):
    def get_students(self):
        query = "SELECT * FROM Students"
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        return users

    def get_student_by_id(self,student_id):
        query = "SELECT * FROM Students WHERE student_id = %s"
        self.cursor.execute(query,(student_id,))
        user = self.cursor.fetchone()
        return user
    
    def update_student(self, student_id, university, degree, graduation_year, resume):
        """
        Update a student's information in the database given their student_id.
        """
        query = """
            UPDATE Students
            SET university = %s,
                degree = %s,
                graduation_year = %s,
                resume = %s
            WHERE student_id = %s
        """
        self.cursor.execute(query, (university, degree, graduation_year, resume, student_id,))
        self.conn.commit()
        return self.cursor.rowcount

    def get_student_info_by_user_id(self, user_id):
        query = "SELECT * FROM Students WHERE student_id = %s"
        self.cursor.execute(query,(user_id,))
        result = self.cursor.fetchone()
        return result
    
    def add_student(self, student_id, university, degree, graduation_year, resume):
        query = "INSERT INTO Students (student_id, university, degree, graduation_year, resume) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(query,(student_id, university, degree, graduation_year, resume))
        self.conn.commit()
        return self.cursor.rowcount