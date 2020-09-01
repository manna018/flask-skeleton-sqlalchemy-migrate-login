from flask import Blueprint

#app/catalog/__init__.py
main=Blueprint('main',__name__,template_folder='templates')



from app.catalog import routes