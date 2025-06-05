from flask import Flask
from flask_mail import Mail
import secrets

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.secret_key = secrets.token_hex(32)
    
    # Email Config (use your Gmail app password)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'tcpsender55@gmail.com'
    app.config['MAIL_PASSWORD'] = 'urjj atkm zftg ikks'

    mail.init_app(app)
    from app.routes import main
    app.register_blueprint(main)
    return app
