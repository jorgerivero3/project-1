from flask import render_template, url_for, flash, redirect, request
from Application import application, db, bcrypt
from Application.forms import RegistrationForm, LoginForm, RequestResetForm, ResetPasswordForm
from Application.models import User
from flask_login import login_user, current_user, logout_user, login_required
import os


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
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Account creation succesful!', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)


@application.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('start_game'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('start_game'))
		else:
			flash('Login unsuccessful. Email and/or password incorrect.')
	return render_template('login.html', title='Login', form=form)


@application.route('/start_game')
def start():
	if current_user.is_authenticated:
		#can start from where they left off
		return
	return render_template('newGame.html', title='Gone to Texas')

@application.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))

@application.route("/password_retrieval", methods=['GET', 'POST'])
def password_retrieval():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RequestResetForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		send_reset_email(user)
		flash('An email has been sent with instructions to reset your password', 'info')
		return redirect(url_for('login'))
	return render_template('password_retrieval.html', title='Reset Password', form=form)


@application.route("/reset_token/<token>", methods=['GET', 'POST'])
def reset_token(token):
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	user = User.verify_reset_token(token)
	if user is None:
		flash('The reset token you are using is invalid or expired.')
		return redirect(url_for('password_retrieval'))
	form = ResetPasswordForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user.password = hashed_password
		db.session.commit()
		flash('Password has been updated.', 'success')
		return redirect(url_for('login'))
	return render_template('reset_token.html', title='Reset Password', form=form)