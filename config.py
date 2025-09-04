import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'student001'  # Change this in production!

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'students.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
