from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def login_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    users = db.relationship('User', backref='roles')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.VARCHAR(32), primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.VARCHAR(255), nullable=False)
    password_hash = db.Column(db.VARCHAR(255), nullable=False)
    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    sex = db.Column(db.INTEGER, nullable=False)
    number = db.Column(db.INTEGER, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    role_id = db.Column(db.INTEGER, db.ForeignKey('roles.id'), default=0, nullable=False)
    programmes = db.relationship('Programme', backref='users')

    def __repr__(self):
        return '<User %r>' % self.username

    # code to transform the password to hash to store in the database,
    # and verify whether the password the user input fit the password hash already stored in th database
    # taken from Grinberg, M. 2018. Flask Web Development: Developing Web Application with Python. 2nd ed. Sebastopol: O’Reilly Media
    # Chapter 8
    @property
    def password(self):
        raise AttributeError('Password is not allowed to access')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        role = Role.query.filter_by(id=self.role_id).first()
        return self.role_id is not None and role.rolename == 'admin'


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.VARCHAR(32), primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    programmes = db.relationship('Programme', backref='categories')

    def __repr__(self):
        return '<Category %r>' % self.name


class Programme(db.Model):
    __tablename__ = 'programmes'
    id = db.Column(db.VARCHAR(32), primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    category_id = db.Column(db.VARCHAR(32), db.ForeignKey('categories.id'), nullable=False)
    age_range = db.Column(db.INTEGER, nullable=False)
    thumbnail = db.Column(db.Text, nullable=False)
    bg_image = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text)
    release_date = db.Column(db.DateTime, default=datetime.utcnow)
    expire_date = db.Column(db.DateTime)
    operator_id = db.Column(db.VARCHAR(32), db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Programme %r>' % self.name
