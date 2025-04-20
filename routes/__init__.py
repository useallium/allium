from routes.api.users import api as users_api
from routes.web.home import web as web_routes

def register_routes(app):
    app.register_blueprint(users_api)
    app.register_blueprint(web_routes)
