import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TFA_CONNECTION_STRING')
    PORT = int(os.environ.get('PORT', 5000))


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    HOST = '127.0.0.1'
    SQLALCHEMY_DATABASE_URI = os.environ.get('TFA_CONNECTION_STRING',
                                             'mssql+pyodbc://@SMOHAMMEDKAMPC/TheFootballApp?'
                                             'driver=SQL+Server&'
                                             'Trusted_Connection=Yes&'
                                             'MultiSubnetFailover=Yes')


class TestingConfig(Config):
    TESTING = True