from routes.api.users import api as users_api
from routes.web.home import web as web_routes
from routes.api.companies import api as companies_api
from routes.web.register import register as register_routes
from routes.web.login import login as login_routes
from routes.web.dashboard import dashboard as dashboard_routes
from routes.api.internships import api as internships_api
from routes.api.login import api as login_api

def init_routes(app):
    app.register_blueprint(users_api)
    app.register_blueprint(web_routes)
    app.register_blueprint(register_routes)
    app.register_blueprint(companies_api)
    app.register_blueprint(login_routes)
    app.register_blueprint(dashboard_routes)
    app.register_blueprint(internships_api)
    app.register_blueprint(login_api)