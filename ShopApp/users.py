from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from ShopApp.models import User
from ShopApp import db

users = Blueprint("users", __name__)


@users.route('/login')
def login():
    if 'user' in session:
        return redirect('hom')
    return render_template('login.html')


@users.route('/logout')
def logout():
    return {"users": []}


@users.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        errors = {}
        data = request.form.to_dict()

        session.permanent = True

        username = data.get('username')
        password = data.get('password')
        password_2 = data.get('password_2')

        if set(list(data.keys())) != set(['username', 'password', 'password_2']):
            errors.update(password="invalid")

        if password != password_2:
            errors.update(password="invalid")

        if errors:
            return redirect('', code=400)
        new_user = User(
            username=username,
            password=password,
        )
        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception:
            pass
        return redirect(url_for('users.login'))
    if 'user' in session:
        user = session['user']
        return render_template('home.html', username=user.username)
    return render_template('sign_up.html')