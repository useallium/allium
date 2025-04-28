from database.base import Database

class Internships(Database):
    def get_all_internships(self):
        """
        Retrieve all published internships
        """

        query = "SELECT * FROM Internships"
        self.cursor.execute(query)
        internships = self.cursor.fetchall()
        return internships
    
    def get_internship_by_id(self,internship_id):
        """
        Retrieve published internships by internship_id
        """
        query = "SELECT * FROM Internships WHERE internship_id = %s"
        self.cursor.execute(query, (internship_id,))
        internship = self.cursor.fetchone()
        return internship
    
    def get_applied_internships_by_student(self,applicant_id):
        """
        Retrieve internships which a student has applied to, given the student_id
        """
        query = "SELECT * FROM Internships WHERE applicant_id = %s"
        self.cursor.execute(query, (applicant_id,))
        applied_internships = self.cursor.fetchall()
        return applied_internships
