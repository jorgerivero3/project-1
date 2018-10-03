from flask import render_template, url_for, flash, redirect, request, abort
from Application import application, db, bcrypt
from Application.forms import RegistrationForm, LoginForm
from Application.models import User
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
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Account creation succesful!', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)


@application.route('.login', methods)
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
	if current_user.is_authenticated:
		#can start from where they left off
	return render_template('newGame.html', title='Gone to Texas')