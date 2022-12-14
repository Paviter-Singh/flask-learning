from turtle import title
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app import app,db
from flask import redirect, render_template, request, flash, redirect, url_for
from app.forms import LoginForm, RegistrationFrom
@app.route('/')
@app.route('/index')
@login_required
def index():
    
    posts = [{"author":{"username":"Jatinder Singh"},
    "body":"It is a beautyful day in poland"},{"author":{"username":"Paviter Singh"},
    "body":"It is a beautyful day in canada"}]
    return render_template('index.html',titel="Home",posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    print(form.username)
    print(form.password.data)
    if form.password.data:
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or passoword')
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc !='':
            next_page = url_for('index')
        # flash('Login requested for user {} remember_me {}'.format(form.username.data,form.remember_me.data))
        return redirect(next_page)
    return render_template(
        'login.html',title="Sign In", form=form
    )
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
@app.route('/test')
def test():
    return render_template('test.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationFrom()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulation new user created")
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)


