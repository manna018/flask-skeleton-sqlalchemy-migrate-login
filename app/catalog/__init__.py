from flask import Blueprint

#app/catalog/__init__.py
main=Blueprint('main',__name__,template_folder='templates')







#must be at bottom to avoid cicular import Perhaps
from app.catalog import routes