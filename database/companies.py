from database.base import Database

class Companies(Database):
    def get_all_companies(self):
        """
        Retrieve all companies
        """
        query = "SELECT * FROM Companies"
        self.cursor.execute(query)
        companies = self.cursor.fetchall()
        return companies
    
    def update_company(self, company_id, address, company_name, email, industry, website):
        """
        Update company information in the database by company_id
        """
        query = """
            UPDATE Companies
            SET address = %s,
                company_name = %s,
                email = %s,
                industry = %s,
                website = %s
            WHERE company_id = %s
        """
        self.cursor.execute(query, (address, company_name, email, industry, website, company_id))
        self.conn.commit()
        return self.cursor.rowcount  # Optional: returns number of rows updated



    def get_company_by_id(self, company_id):
        """
        Retrieve company by company_id
        """
        query = "SELECT * FROM Companies WHERE company_id = %s"  # Use %s placeholder
        self.cursor.execute(query, (company_id,))  # Pass parameters as a tuple
        company = self.cursor.fetchone()
        return company
    
    def add_company(self, address,company_name, email, industry, website):
        """
        Add company to the database given address, company_name, email, industry, website
        """
        query = """INSERT INTO Companies (address, company_name, email, industry, website) VALUES (%s, %s, %s, %s, %s)"""
        self.cursor.execute(query,(address,company_name,email,industry,website))
        company_id = self.cursor.lastrowid
        return company_id

    def returnstr():
        return "hello"




