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
    
    def add_internship(self, company_id, recruiter_id, title, description, location, is_remote,
                department, start_date, end_date, is_paid, salary, is_filled):
        """
        add a new internship to the database
        """
        query = """INSERT INTO Internships (company_id, recruiter_id, title, description, location, is_remote,
                department, start_date, end_date, is_paid, salary, is_filled) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        self.cursor.execute(query,(company_id,recruiter_id,title,description,location,is_remote,department,start_date,end_date,is_paid,salary,is_filled))
        self.conn.commit()
        internship_id = self.cursor.lastrowid
        return internship_id
    
    def remove_internship(self, internship_id):
        query = "DELETE FROM Internships WHERE internship_id = %s"
        self.cursor.execute(query,(internship_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def update_internship(self, internship_id, title, description, location, is_remote, department, start_date, end_date, is_paid, salary, is_filled):
        """
        Update internship information in the database by internship_id
        """
        query = """
            UPDATE Internships
            SET title = %s,
                description = %s,
                location = %s,
                is_remote = %s,
                department = %s,
                start_date = %s,
                end_date = %s,
                is_paid = %s,
                salary = %s,
                is_filled = %s,
                updated_at = NOW()
            WHERE internship_id = %s
        """
        self.cursor.execute(query, (
            title,
            description,
            location,
            is_remote,
            department,
            start_date,
            end_date,
            is_paid,
            salary,
            is_filled,
            internship_id
        ))
        self.conn.commit()
        return self.cursor.rowcount