from database.base import Database

class Applications(Database):
    def get_applications(self):
        query = "SELECT * FROM Applications"
        self.cursor.execute(query)
        applications = self.cursor.fetchall()
        return applications
    
    def get_applications_by_student(self, applicant_id):
        query = "SELECT * FROM Applications WHERE applicant_id = %s"
        self.cursor.execute(query, (applicant_id))
        applications = self.cursor.fetchall()
        return applications
    
    def get_applications_by_internship(self, internship_id):
        query = "SELECT * FROM Applications WHERE internship_id = %s"
        self.cursor.execute(query,(internship_id))
        internship_applications = self.cursor.fetchall()
        return internship_applications

    def get_application_by_application_id(self, application_id):
        query = "SELECT * FROM Applications WHERE application_id = %s"
        self.cursor.execute(query,(application_id,))
        application = self.cursor.fetchone()
        return application
    
    def update_application_status(self, status, application_id):
        query = """UPDATE Applications SET status = %s WHERE application_id = %s"""
        self.cursor.execute(query,(status,application_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0