from app.auth import auth_bp
from app.catalog.models import Funny
from flask import render_template
from app import login_manager
from flask_login import login_user,logout_user,current_user,login_required


@auth_bp.route('/checkUser')
def checkUser():
    return "Checking"

@auth_bp.route("/currentUser")
@login_required 
def curUser():
    return "Current User"+str(current_user)

@auth_bp.route("/checkHead")
def checkHead():
    return render_template('checkHead.html')