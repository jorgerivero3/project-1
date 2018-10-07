from Application import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin): #possibly link to character?
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	characters = db.relationship('Character', backref='username', lazy=True) #eager=True) need to figure this out

	'''
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
	'''

	def __repr__(self):
		return f"User('{self.username}')"

class Character(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	characterName = db.Column(db.String(15), nullable=False)
	health = db.Column(db.Integer, nullable=False, default=100)
	alive = db.Column(db.Boolean, nullable=False, default=True)
	progress = db.Column(db.Integer, nullable=False, default=0)
	user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
		
	def __repr__(self):
		return f"Character('{self.characterName}', '{self.progress}')"
