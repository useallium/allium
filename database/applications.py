from database.base import Database

class Applications(Database):
    def get_applications(self):
        query = "SELECT * FROM Applications"
        self.cursor.execute(query)
        applications = self.cursor.fetchall()
        self.conn.close()
        return applications
    
    def get_applications_by_student(self, applicant_id):
        query = """SELECT
        Internships.*,
        Companies.*,
        Applications.*
        FROM
        Applications
        JOIN
        Internships ON Applications.internship_id = Internships.internship_id
        JOIN
        Companies ON Internships.company_id = Companies.company_id
        WHERE
        Applications.applicant_id = %s;"""
        self.cursor.execute(query, (applicant_id,))
        applications = self.cursor.fetchall()
        self.conn.close()
        return applications
    
    def get_applications_by_internship(self, internship_id):
        query = """
            SELECT 
                Applications.*,
                Students.university,
                Students.degree,
                Students.graduation_year,
                Students.resume
            FROM Applications
            JOIN Students ON Applications.applicant_id = Students.student_id
            WHERE Applications.internship_id = %s
        """
        self.cursor.execute(query, (internship_id,))
        return self.cursor.fetchall()



    def get_application_by_application_id(self, application_id):
        query = "SELECT * FROM Applications WHERE application_id = %s"
        self.cursor.execute(query,(application_id,))
        application = self.cursor.fetchone()
        self.conn.close()
        return application#
    
    def update_application_status(self, status, application_id):
        query = """UPDATE Applications SET status = %s WHERE application_id = %s"""
        self.cursor.execute(query,(status,application_id,))
        self.conn.commit()
        self.conn.close()
        return self.cursor.rowcount > 0
    
    def remove_application(self, application_id):
        query = "DELETE FROM Applications WHERE application_id = %s"
        self.cursor.execute(query,(application_id,))
        self.conn.commit()
        self.conn.close()
        return self.cursor.rowcount > 0
    
    
    def apply(self, applicant_id, internship_id, resume):
        query = "INSERT INTO Applications (applicant_id, internship_id, resume) VALUES (%s,%s,%s)"
        self.cursor.execute(query,(applicant_id,internship_id,resume,))  
        self.conn.commit()
        self.conn.close()
        return self.cursor.rowcount > 0 
    

