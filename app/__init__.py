# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db=SQLAlchemy()
migrate=Migrate()
def create_app(config_type):
    app=Flask(__name__)
    print(config_type)
    configuration=os.path.join(os.getcwd(),'config',os.getenv('FLASK_ENV','dev')+'.py') #export FLASK_ENV=dev/prod
    app.config.from_pyfile(configuration)
    db.init_app(app)
    migrate.init_app(app,db)
    from app.catalog import main
    app.register_blueprint(main)
    return app
