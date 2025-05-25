from database.base import connect

class Internships:
    def get_all_internships(self):
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        try:
            query = "SELECT * FROM Internships"
            cursor.execute(query)
            internships = cursor.fetchall()
            return internships
        finally:
            cursor.close()
            conn.close()
    
    def get_internships_by_recruiter(self, recruiter_id):
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        try:
            query = "SELECT * FROM Internships WHERE recruiter_id = %s"
            cursor.execute(query, (recruiter_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()
    
    def get_applicants_for_internship(self, internship_id):
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        try:
            query = """
                SELECT 
                    A.application_id,
                    A.status,
                    A.resume AS application_resume,
                    A.applied_at,
                    S.student_id,
                    S.university,
                    S.degree,
                    S.graduation_year,
                    S.resume AS student_resume
                FROM Applications A
                JOIN Students S ON A.applicant_id = S.student_id
                WHERE A.internship_id = %s
            """
            cursor.execute(query, (internship_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()
    
    def get_internship_by_id(self, internship_id):
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        try:
            query = "SELECT * FROM Internships WHERE internship_id = %s"
            cursor.execute(query, (internship_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    def add_internship(self, company_id, recruiter_id, title, description, location, is_remote,
                       department, start_date, end_date, is_paid, salary, is_filled):
        conn = connect()
        cursor = conn.cursor()
        try:
            query = """
                INSERT INTO Internships 
                (company_id, recruiter_id, title, description, location, is_remote,
                 department, start_date, end_date, is_paid, salary, is_filled) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            cursor.execute(query, (company_id, recruiter_id, title, description, location, is_remote,
                                   department, start_date, end_date, is_paid, salary, is_filled))
            conn.commit()
            return cursor.lastrowid
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

    def update_internship(self, internship_id, title, description, location, is_remote, department,
                          start_date, end_date, is_paid, salary, is_filled):
        conn = connect()
        cursor = conn.cursor()
        try:
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
            cursor.execute(query, (title, description, location, is_remote, department,
                                   start_date, end_date, is_paid, salary, is_filled, internship_id))
            conn.commit()
            return cursor.rowcount
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

    def remove_internship(self, internship_id):
        conn = connect()
        cursor = conn.cursor()
        try:
            query = "DELETE FROM Internships WHERE internship_id = %s"
            cursor.execute(query, (internship_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

    def get_company_by_internship(self, internship_id):
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        try:
            query = """
                SELECT Companies.company_name
                FROM Companies
                JOIN Internships I ON Companies.company_id = I.company_id
                WHERE I.internship_id = %s
            """
            cursor.execute(query, (internship_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    
