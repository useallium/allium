from database.base import Database

class Students(Database):
    def get_students(self):
        query = "SELECT * FROM Students"
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        return users
    
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
        self.cursor.execute(query, (university, degree, graduation_year, resume, student_id))
        self.conn.commit()
        return self.cursor.rowcount 
            