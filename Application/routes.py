from flask import render_template, url_for, flash, redirect, request
from Application import application, db, bcrypt, mail
from Application.forms import RegistrationForm, LoginForm, RequestResetForm, ResetPasswordForm, UpdateInfo, GameInput
from Application.models import User
from flask_login import login_user, current_user, logout_user, login_required
import os
from Application.levels import master
from flask_mail import Message


@application.route('/')
def home():
	return render_template('/home.html', title='The UT Trail')


@application.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('game'))
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
		return redirect(url_for('game'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(url_for('game'))
		else:
			flash('Login unsuccessful. Email and/or password incorrect.')
	return render_template('login.html', title='Login', form=form)

@application.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateInfo()
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('Info Updated', 'success')
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
	return render_template('account.html', title='Account Information', form=form)

@application.route('/about')
def about():
	return render_template('/about.html', title='About The UT Trail')


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

def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
	msg.body = f''' To reset your password, click the following link, or copy and
paste it into your web browser:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then please ignore this email.
'''
	mail.send(msg)

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


			#############################
			######### GAME CODE #########
			#############################

@application.route('/game', methods=['GET', 'POST'])
@login_required
def game():
	if current_user.progress == 'gg':
		return redirect(url_for('gameover'))
	else:
		pageDetails = get_level(current_user.progress)
		form = GameInput()
		if form.validate_on_submit():
			index = int(form.ans.data) - 1 #arrays start at 0
			eff = pageDetails.effects[index]
			doEffect(eff)
			current_user.progress = pageDetails.progress[index]
			db.session.commit()
			return redirect(url_for('game'))
	return render_template('UTtrailGame.html', title='hookem', form=form, prompts=[pageDetails.story, pageDetails.prompts])

def get_level(progress):
	return master[progress]

def doEffect(array):
	for string in array:
		if string == '':
			return
		else:
			if string[-1] == 'h':
				if string[0] == '+':
					current_user.health = current_user.health + int(string[1:-2])
				else:
					current_user.health = current_user.health - int(string[1:-2])
			elif string[-1] == 's':
				if string[0] == '+':
					current_user.sanity = current_user.sanity + int(string[1:-2])
				else:
					current_user.sanity = current_user.sanity - int(string[1:-2])
			else:
				if string[0] == '+':
					current_user.grades = current_user.grades + int(string[1:-2])
				else:
					current_user.grades = current_user.grades - int(string[1:-2])
			if current_user.health > 100:
				current_user.health = 100
			if current_user.sanity > 100:
				current_user.sanity = 100
			if current_user.grades > 100:
				current_user.grades = 100
			return


@application.route('/gameover')
@login_required
def gameover():
	return render_template('gameover.html', health=current_user.health, sanity=current_user.sanity, grades=current_user.grades)
