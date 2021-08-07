from re import template
from flask import Blueprint, render_template
from marvel_api.forms import UserForm

auth = Blueprint('auth', __name__, template_folder='auth_templates')



@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserForm()
    return render_template('signup.html', form = form)

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = UserForm()
    return render_template('signin.html', form = form)