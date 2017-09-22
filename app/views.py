from flask import Flask, render_template, request,url_for, redirect
from app.my_app import app
from app.controller import RegisterForm, CreateShoppingItem, LoginForm, CreateShoppingItem
from app.models.user import User
from passlib.hash import sha256_crypt
from flask_login import login_user, login_required

app.config['SECRET_KEY']  = 'itsmysecret'

@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Returns the register UI. """
    form = RegisterForm(request.form)
    if request.method == 'POST':
        username = form.username.data
        email = form.email.data
        password = form.password.data
        # confirm_password = form.confirm_password.data
        new_user = User(username, email, password)
        print(new_user.user_id, str(new_user.password), new_user.email)
        # new_user.compare_password()
        if  User.email_exists(new_user):
            error="Account exists. Sign in to the account"
            return render_template("signup.html", error=error)
        new_user.registration_store()
        return redirect(url_for('login'))
    return render_template("signup.html", form= form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    """ Enable user to login his her credentia;s """
    form = LoginForm(request.form)
    if request.method=='POST':
        email = form.email.data
        password = form.password.data
        
        auth_user = User.signin(email, password)
        print(email, password)
        print(auth_user)
        if auth_user is False:
            error = "Login unsuccessful. Please retry "
            return render_template("signin.html",form=form, error=error)
        redirect(url_for('view_shopping_list'))
    return render_template("signin.html", form = form)

@app.route('/shopping-list/')
def view_shopping_list():
    return render_template("shopping_list.html")

@app.route('/shopping-item')
def view_shopping_item():
    return render_template("shopping_items.html")
