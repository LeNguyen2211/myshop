from flask import Blueprint, render_template, request, flash, redirect
from ShopApp.models import User
from ShopApp import db

users = Blueprint("user", __name__)


@users.route('/login')
def login():
    return {"users": []}


@users.route('/logout')
def logout():
    return {"users": []}


@users.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        data = request.form.to_dict()
        if set(list(data.keys())) != set(['username', 'password', 'password_2']):
            flash("Can not regis account")
        username = data.get('username')
        password = data.get('password')
        password_2 = data.get('password_2')
        if password != password_2:
            flash("Password 2 invalid!")
        new_user = User(
            username=username,
            password=password,
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Create user account success!")
        except Exception:
            pass
        return redirect('/sign_up', code=200)

    return render_template('sign_up.html')


