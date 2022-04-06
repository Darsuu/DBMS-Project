# Makes the website folder a python package
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'G13F34ufnerubf3'

    from .views import views
    
    app.register_blueprint(views, url_prefix='/')

    return app