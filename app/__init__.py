# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db=SQLAlchemy()
migrate=Migrate()
login_manager=LoginManager()
# login_manager.login_view='catalog.do_login'
login_manager.blueprint_login_views={
    'login':'/login',
    'currentUser':'/currentUser',
}
bcrypt=Bcrypt()

def create_app(config_type):
    app=Flask(__name__)
    print(config_type)
    configuration=os.path.join(os.getcwd(),'config',os.getenv('FLASK_ENV','dev')+'.py') #export FLASK_ENV=dev/prod
    app.config.from_pyfile(configuration)
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)
    bcrypt.init_app(app)


    from app.catalog import main
    app.register_blueprint(main)
    from app.auth import auth_bp
    app.register_blueprint(auth_bp)
    return app
