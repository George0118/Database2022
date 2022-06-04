from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import MySQLdb

db = SQLAlchemy()
DB_NAME = "mydb"

client = MySQLdb.connect(host = "127.0.0.1", port = 3306, user = "root", passwd = "", db = "mydb")

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello there'

    client = MySQLdb.connect(host = "127.0.0.1", port = 3306, user = "root", passwd = "", db = "mydb")

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app