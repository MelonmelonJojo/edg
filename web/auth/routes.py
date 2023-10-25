from datetime import datetime
from flask import render_template, session, redirect, url_for
from ..main import main
from ..main.forms import LoginForm, RegisterForm
from . import auth
from .. import db
from ..models import User
from flask_login import login_required


@auth.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@auth.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'


# code to direct to the register page and allow users to register
# taken from Grinberg, M. 2018. Flask Web Development: Developing Web Application with Python. 2nd ed. Sebastopol: O’Reilly Media
# Chapter 8
# Added code to set user id automatically as a 32 length uuid
# Added code to detect whether the user data commit successfully and send the result as a message to the front-end
# Added code to authenticate the registered user and login the page directly with redirecting to the home page
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)
