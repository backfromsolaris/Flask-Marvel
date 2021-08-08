from flask_sqlalchemy import SQLAlchemy
import uuid
import secrets
from flask_login import UserMixin, LoginManager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow


ma = Marshmallow()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True, unique = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    user_name = db.Column(db.String, nullable = False)
    owner_token = db.Column(db.String, nullable = False, unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, password, user_name, owner_token = '', id = ''):
        self.id = self.set_id()
        self.email = email
        self.password = self.set_password(password)
        self.user_name = user_name
        self.owner_token = self.set_token(24)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def set_token(self, length):
        return secrets.token_hex(length)

class Hero(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True, unique = True)
    hero_name = db.Column(db.String(150), nullable = False)
    description = db.Column(db.String(200))
    comics_appeared_in = db.Column(db.Numeric(precision=6, scale=0))
    super_power = db.Column(db.String(150))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    owner_token = db.Column(db.String, db.ForeignKey('user.owner_token'), nullable = False)

    def __init__(self,hero_name,description,comics_appeared_in,super_power,owner_token):
        self.id = self.set_id()
        self.hero_name = hero_name
        self.description = description
        self.comics_appeared_in = comics_appeared_in
        self.super_power = super_power
        self.owner_token = owner_token
    
    def set_id():
        return (secrets.token_urlsafe())

class HeroSchema(ma.Schema):
    class Meta:
        fields = ['id','hero_name','description','comics_appeared_in','super_power','date_created']

hero_schema = HeroSchema()
heroes_schema = HeroSchema(many=True)