import os

from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "Gandalf the Grey"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False