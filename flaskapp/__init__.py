from flask import Flask

def create_app():
    """ Creates flask app """
    app = Flask(__name__)

    from .routes import bp_api

    app.register_blueprint(bp_api, url_prefix='/api')

    return app