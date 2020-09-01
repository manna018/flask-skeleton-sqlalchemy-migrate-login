import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG=True
SECRET_KEY='hii'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')