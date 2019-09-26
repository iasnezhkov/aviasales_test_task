import os

APP_ROOT_FOLDER = os.path.join(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))


class Base(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'i_dont_want_my_cookies_expiring_while_developing_yep'
    FILE_STORAGE = os.path.join(APP_ROOT_FOLDER, 'raw_data')


class DevelopmentConfig(Base):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost:5432/postgres'


class TestingConfig(Base):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'


class ProductionConfig(Base):
    DEBUG = False
    TESTING = False
    POSTGRES_USERNAME = os.environ.get('POSTGRES_USERNAME', 'postgres')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
    POSTGRES_HOSTNAME = os.environ.get('POSTGRES_HOSTNAME', 'postgres')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '5432')
    POSTGRES_DB_NAME = os.environ.get('POSTGRES_DB_NAME', 'postgres')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{username}:{password}@{host}:{port}/{database_name}'.format(
        username=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOSTNAME,
        port=POSTGRES_PORT,
        database_name=POSTGRES_DB_NAME)
