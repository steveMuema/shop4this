from flask import Flask, render_template, request,url_for, redirect
from app import app
from app.controller import RegisterForm, CreateShoppingItem, LoginForm, CreateShoppingItem
from app.models.user import User
from passlib.hash import sha256_crypt
from flask_login import login_user, login_required

app.config['SECRET_KEY']  = 'itsmysecret'

@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Returns the register UI. """
    form = RegisterForm(request.form)
    if request.method == 'POST':
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))
        confirm_password = sha256_crypt.encrypt(str(form.confirm_password.data))
        new_user = User(username, email, password, confirm_password)
        print(new_user.user_id, str(new_user.password), new_user.confirm_password)
        if  User.email_exists(new_user):
            error="Account exists. Sign in to the account"
            return render_template("signup.html", error=error)
        new_user.compare_password()
        new_user.registration_store()
        return redirect(url_for('login'))
    return render_template("signup.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    
    form = LoginForm(request.form)
    if request.method=='POST':
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))
        auth_user = User.signin(email, password)
        # print(auth_user)
        # if User.signin(email, password):
        #     error = "Login unsuccessful. Please retry "
        #     return render_template("signin.html", error=error)
        # login_user(auth_user)
        redirect(url_for('view_shopping_list'))
    return render_template("signin.html")

@app.route('/shopping-list/')
def view_shopping_list():
    return render_template("shopping_list.html")

@app.route('/shopping-item')
def view_shopping_item():
    return render_template("shopping_items.html")
