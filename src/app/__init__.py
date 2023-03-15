from flask import Flask
from .controllers.view.general import bp as view_bp

server = Flask(__name__)
server.register_blueprint(view_bp)
