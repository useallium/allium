from database.base import Database

class Recruiters(Database):
    def get_all_recruiters(self):
        """
        Retrieve all recruiters from the database.
        """
        query = "SELECT * FROM Recruiters"
        self.cursor.execute(query)
        recruiters = self.cursor.fetchall()
        return recruiters

    def get_recruiter_by_id(self, recruiter_id):
        """
        Retrieve a specific recruiter by recruiter_id.
        """
        query = "SELECT * FROM Recruiters WHERE recruiter_id = %s"
        self.cursor.execute(query, (recruiter_id,))
        recruiter = self.cursor.fetchone()
        return recruiter

    def update_recruiter(self, recruiter_id, job_title, phone_number):
        """
        Update a recruiter's information in the database.
        """
        query = """
            UPDATE Recruiters
            SET job_title = %s,
                phone_number = %s
            WHERE recruiter_id = %s
        """
        self.cursor.execute(query, (job_title, phone_number, recruiter_id))
        self.conn.commit()
        return self.cursor.rowcount  # Number of rows updated
