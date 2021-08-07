from re import template
from flask import Blueprint, render_template, request
from marvel_api.forms import UserForm

auth = Blueprint('auth', __name__, template_folder='auth_templates')



@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserForm()
    if request.method == 'POST' and form.validate_on_submit():
        user_name = form.user_name.data
        password = form.password.data
        email = form.email.data
        print(user_name, email, password)
    return render_template('signup.html', form = form)

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = UserForm()
    if request.method == 'POST' and form.validate_on_submit():
        user_name = form.user_name.data
        password = form.password.data
        email = form.email.data
        print(user_name, email, password)
    return render_template('signin.html', form = form)