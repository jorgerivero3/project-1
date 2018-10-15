from Application import db, login_manager, application
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	#character/game details not changeable by user
	health = db.Column(db.Integer, nullable=False, default=100)
	sanity = db.Column(db.Integer, nullable=False, default=100)
	grades = db.Column(db.Integer, nullable=False, default=100)
	progress = db.Column(db.String(2), nullable=False, default='a1')

	def get_reset_token(self, expires_sec=1800):
		s = Serializer(application.config['SECRET_KEY'], expires_sec)
		return s.dumps({'user_id': self.id}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(application.config['SECRET_KEY'])
		try:
			user_id = s.loads(token)['user_id']
		except:
			return None
		return User.query.get(user_id)

	def is_dead(self):
		return self.health <= 0

	def __repr__(self):
		return f"User('{self.username}', '{self.health}', '{self.sanity}', '{self.grades}')"
