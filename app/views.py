import json
from flask import Flask, render_template, request,url_for, redirect, session, flash
from app.my_app import app
from functools import wraps
from app.controller import RegisterForm, LoginForm, CreateProductItem, UpdateProfile
from app.models.user import User
from app.models.my_products import MyProduct
from flask_login import login_user, login_required

app.config['SECRET_KEY']  = 'itsmysecret'

def read_user_json_dumps():
    with open("user_data_dumps.json", "r") as readfile:
        users_data = json.load(readfile)
        return users_data
# Check if user logged in
def is_logged_in(param):
    @wraps(param)
    def wrap(*args, **kwargs):
        if  'logged_in' in session:
            return param(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Returns the register UI. """
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        new_user = User(str(username), str(email), str(password))
        new_user.registration_store()
        session['logged_in'] = True
        session['email'] = email
        return redirect(url_for('login'))       
    return render_template("signup.html", form= form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    """ Enable user to login his her credentials """
    all_users = read_user_json_dumps()
    session['logged_in'] = True
    form = LoginForm(request.form)
    if request.method=='POST':
        email = form.email.data
        password = form.password.data
        auth_email = all_users['email']
        auth_pswd = all_users['password']
        auth_account=(auth_email, auth_pswd)     
        auth_input = (str(email), str(password))
        if auth_account != auth_input:
            error = "Login unsuccessful. Please retry "
            return render_template("signin.html",form=form, error=error)
        return redirect(url_for('update_user', user_id = all_users['user_id']))
    return render_template("signin.html", form = form)

@app.route('/profile/<user_id>', methods=['GET', 'POST'])
@is_logged_in
def update_user(user_id):
    """" User can create and view their shopping lists """
    user_data = read_user_json_dumps() 
    form = UpdateProfile(request.form)
    if request.method == 'POST' and form.validate():
        business_no = form.business_no.data
        phone_no = form.phone_no.data
        #TODO: pass data to the dumps and update
        return redirect(url_for('my_products', user_id=user_data['user_id']))
    return render_template("profile.html", form=form)

@app.route('/<user_id>/my_products')
@is_logged_in
def my_products(user_id):
    """Show a list of user products and allow CRUD operations on th data"""
    form = CreateProductItem(request.form)
    return render_template("my_products.html", form =form)


@app.route('/create_product', methods = ['GET', 'POST'])
@is_logged_in
def create_product(product_name, product_price):
    """ User can create and view their shopping list items"""
    form =  CreateProductItem(request.form)
    if request.method == 'POST' and form.validate():
        product_name = form.product_name.data
        product_price = form.product_price.data
        new_product = MyProduct( product_name, product_price)
        new_product.my_products_store()
    return render_template('shopping_items.html',  form=form,)

@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))
