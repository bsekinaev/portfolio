import os

class Config:
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///portfolio.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Настройки почты
    MIIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = os.environ.get('bsekinaev@gmail.com')
    MAIL_PASSWORD = os.environ.get('password')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')
    