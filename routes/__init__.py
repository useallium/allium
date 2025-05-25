from routes.web.home import web as web_routes
from routes.web.dashboard import dashboard as dashboard_routes
from routes.web.internships import internships as internship_routes
from routes.web.auth import auth
from routes.web.users import profile as profile_routes
from routes.web.recruiters import recruiter as recruiter_routes 
from routes.api.users import api as users_api
from routes.api.companies import api as companies_api
from routes.api.internships import api as internships_api
from routes.api.login import api as login_api
from routes.api.application import api as application_api


def init_routes(app):
    app.register_blueprint(web_routes)
    app.register_blueprint(dashboard_routes)
    app.register_blueprint(auth)
    app.register_blueprint(profile_routes)
    app.register_blueprint(internship_routes)
    app.register_blueprint(users_api)
    app.register_blueprint(companies_api)
    app.register_blueprint(internships_api)
    app.register_blueprint(login_api)
    app.register_blueprint(application_api)
    app.register_blueprint(recruiter_routes)
