from flask import Blueprint

#app/auth/__init__.py
auth_bp=Blueprint('auth_bp',__name__,template_folder='templates')







#must be at bottom to avoid cicular import Perhaps
from app.auth import routes