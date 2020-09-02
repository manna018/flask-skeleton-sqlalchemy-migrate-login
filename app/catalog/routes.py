from app.catalog import main
from app import db
from app.catalog.models import Book,Publication,Funny
from flask import render_template
from app import login_manager
from flask_login import login_user,logout_user


@main.route('/')
def display_books():
    books=Book.query.all()
    return render_template('home.html',books=books)

@main.route('/login')
def do_login():
    fun=Funny(name='mohit',phno='1234')
    try:
        login_user(fun,True)
    except Exception as e:
        return "Failed"
    return "Gud"

