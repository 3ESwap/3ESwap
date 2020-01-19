from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

#app = Flask(__name__, template_folder='../templates', static_url_path='', static_folder='../templates')
app = Flask(__name__, template_folder='../client', static_url_path='', static_folder='../client')
app.config['SECRET_KEY'] = 'a0e3969c13f75e6e6b51d3b154b21839'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from server import routes