from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from flask_mail import Mail

application = Flask(__name__)
application.config['SECRET_KEY'] = 'c435bd07880364149cdf9661f1994db4'
''' idk what this stuff does either
application.config['SQLALCHEMY_DATABASE_URI'] = [something here]
application.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
application.secret_key = "zvXzBQR8oBB5kgKpQH1xC5Sf0hSEz8l/CwQKA9VM"
'''

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)

login_manager = LoginManager(application)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

''' idk how the mail stuff works
application.config['MAIL_SERVER'] = 'smtp.googlemail.com'
application.config['MAIL_PORT'] = 587
application.config['MAIL_USE_TLS'] = True
application.config['MAIL_USERNAME'] = 'cs329efall18project1'
application.config['MAIL_PASSWORD'] = 'texascompsci18'
mail = Mail(application)
'''

from Application import routes