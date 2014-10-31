import os

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = 'test.db'
SECRET_KEY = 'my precious'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
