from flask import Blueprint, jsonify, request
from database.companies import Companies

api = Blueprint('companies_api', __name__, url_prefix='/api')


#RETURN ALL COMPANIES
@api.route('/companies', methods=['GET'])
def get_companies():
    db = Companies()
    try:
        companies = db.get_all_companies()
        return jsonify(companies)
    except:
        return jsonify("failed to fetch companies")
    


#RETURN COMPANY BY GIVEN ID
@api.route('/companies/<int:company_id>', methods=['GET'])
def get_company(company_id):
    print("company_id:", company_id)  # This is just for debugging; you can remove it later.
    db = Companies()
    try:
        company = db.get_company_by_id(company_id)
        if company:
            return jsonify(company)  # Return company data
        else:
            return jsonify({"error": "Company not found"}), 404  # Handle case where no company is found
    except Exception as e:
        print(f"Error fetching company: {e}")  # Log the error for debugging
        return jsonify({"error": "Failed to fetch company"}), 500


#ADD A NEW COMPANY
@api.route('/companies/add', methods=['POST'])
def add_company():
    db = Companies()
    try:

        data = request.get_json()

        company = {
            "address": data.get('address'),
            "company_name": data.get('company_name'),
            "email":data.get('email'),
            "industry":data.get('industry'),
            "website":data.get('website')
        }

        print(company)

        retrieve_id = db.add_company(company['address'], company['company_name'],company['email'],company['industry'],company['website'])
        #return jsonify({"message":"success", "company_info":{"company_id":1000000, "company_info":company}})
        if retrieve_id != None:
            return jsonify({"message":"success", "company_info":{"company_id":retrieve_id, "company_info":company}})

    except Exception as e:
        return jsonify({"error":"failed to add company to database"}), 500
    
@api.route('/companies/update', methods=['POST'])
def update_company():
    db = Companies()
    try:
        data = request.get_json()

        company = {
            "address": data.get('address', None),
            "company_name": data.get('company_name',None),
            "email":data.get('email',None),
            "industry":data.get('industry,None'),
            "website":data.get('website',None)
        }

        print(company)

        return jsonify(company)


    except Exception as e:
        pass