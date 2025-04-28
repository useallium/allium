from flask import Blueprint, jsonify, request
from database.companies import Companies

api = Blueprint('companies_api', __name__, url_prefix='/api')


@api.route('/companies', methods=['GET'])
def get_companies():
    db = Companies()
    try:
        companies = db.get_all_companies()
        return jsonify(companies)
    except:
        return jsonify("failed to fetch companies")
    
# In the Flask route
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



# @api.route('/companies/add', methods=['POST'])
# def add_companies():
#     conn = connect()
#     cursor = conn.cursor(dictionary=True)

#     data = request.get_json()

#     address = data.get('address')
#     company_name = data.get('company_name')
#     email = data.get('email')
#     industry = data.get('industry')
#     website = data.get('website')

#     print(data)

#     if not address or not company_name or not email or not industry or not website:
#         return jsonify({'message': 'Missing required fields'}), 400

#     try:

#         cursor.execute("""
#         INSERT INTO Companies (address, company_name, email, industry, website) VALUES (%s, %s, %s, %s, %s)
#         """, (address, company_name, email, industry, website))

#         conn.commit()

#         company_id = cursor.lastrowid

#     # Return success response with the newly created user's details
#         return jsonify({
#             'message': 'User created successfully',
#             'company_id': company_id,
#             'email': email,
#             'company_name': company_name,
#             'address': address,
#             'industry': industry,
#             'website': website,
#         }), 201

#     except Exception as e:
#         return jsonify({'message': str(e)}), 500