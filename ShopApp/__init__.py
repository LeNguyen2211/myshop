import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


db = SQLAlchemy()


from ShopApp.views import views
from ShopApp.users import users

# load env file
load_dotenv()

DB_NAME = os.environ['DB_NAME']
SECRET_KEY = os.environ['SECRET_KEY']


def create_database(app):
    if not os.path.exists(f'ShopApp/{DB_NAME}.db'):
        db.create_all(app=app)
        print("Database created!")


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}.db"
    db.init_app(app)

    from ShopApp.models import User, Product, ProductType
    create_database(app)

    app.register_blueprint(views)
    app.register_blueprint(users)
    return app
