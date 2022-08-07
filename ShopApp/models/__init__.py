from .. import db
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_time = db.Column(db.DateTime(timezone=True), default=func.now(), onupdate=func.now())


class User(BaseModel):
    __tablename__ = "user"

    username = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    location = db.Column(db.String(255))
    phone_number = db.Column(db.String(50))

    def __init__(self, username, password, email=None):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)


class ProductType(BaseModel):
    __tablename__ = "product_type"

    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    products = db.relationship('Product')


class Product(BaseModel):
    __tablename__ = "product"

    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    price = db.Column(db.Integer())
    product_type = db.Column(db.Integer, db.ForeignKey("product_type.id"))
