from flask import render_template, url_for, flash, redirect, request, abort
from Application import application, db, bcrypt
from Application.forms import RegistrationForm, LoginForm
#import models
from flask_login import login_user, current_user, logout_user, login_required

@application.route('/')
def home():
	if current_user.is_authenticated:
		return redirect(url_for('start_game'))
	return render_template('/home.html', title='The UT Trail')


@application.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('start_game'))
	form = RegistrationForm()
	if form.validate_on_submit():

@application.route('/start_game')
	if current_user.is_authenticated: