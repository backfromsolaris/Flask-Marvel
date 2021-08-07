from re import template
from flask import Blueprint, render_template, request, redirect, url_for, flash
from marvel_api.forms import UserForm
from marvel_api.models import db, User, check_password_hash
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__, template_folder='auth_templates')



@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserForm()
    if request.method == 'POST' and form.validate_on_submit():
        user_name = form.user_name.data
        password = form.password.data
        email = form.email.data
        print(user_name, email, password)
        new_user = User(email, password, user_name)
        db.session.add(new_user)
        db.session.commit()
        flash(f'{user_name} - You have successfully created a user account with {email}!', 'user-created')
        return redirect(url_for('site.home'))
    return render_template('signup.html', form = form)

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = UserForm()
    if request.method == 'POST' and form.validate_on_submit():
        password = form.password.data
        email = form.email.data
        print(email, password)
        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            user_name = logged_user.user_name
            login_user(logged_user)
            flash(f'{user_name} - You have successfully logged in with {email}!', 'auth-success')
            return redirect(url_for('site.home'))
        else:
            flash('Your login credentials are incorrect', 'auth-failed')
            return redirect(url_for('auth.signin'))

    return render_template('signin.html', form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f'You have successfully logged out!', 'auth-success')
    return redirect(url_for('site.home'))