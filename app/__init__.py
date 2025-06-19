from flask import Flask
from .routes import calculator_bp

def create_app():
    app = Flask(__name__,
                template_folder='templates',
                static_folder='static')
    app.register_blueprint(calculator_bp)
    return app