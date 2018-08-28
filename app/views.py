import json
from flask import Flask, render_template, request,url_for, redirect, session, flash
from app.my_app import app
from functools import wraps
from app.controller import RegisterForm, CreateShoppingList, LoginForm, CreateShoppingItem, EditShoppingList, EditShoppingItem, UpdateProfile
from app.models.user import User
from app.models.shopping_list import Shopping_list
from app.models.shopping_item import Shopping_item
from flask_login import login_user, login_required

app.config['SECRET_KEY']  = 'itsmysecret'

def read_json_dumps():
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
        if  User.email_exists(new_user):
            error="Account exists. Sign in to the account"
            return render_template("signup.html", error=error)
        new_user.registration_store()
        session['logged_in'] = True
        session['email'] = email
        return redirect(url_for('login'))       
    return render_template("signup.html", form= form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    """ Enable user to login his her credentials """
    all_users = read_json_dumps()
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
    user_data = read_json_dumps() 
    form = UpdateProfile(request.form)
    if request.method == 'POST' and form.validate():
        business_no = form.business_no.data
        phone_no = form.phone_no.data
        if user_data["user_id"] == user_id:
            user_data["business_no" ] = business_no
            user_data["phone_no" ] = phone_no
    return render_template("profile.html", form=form)


@app.route('/delete_list/<list_id>')
@is_logged_in
def delete_list(list_id):
    """ Link to do a delete method call"""
    Shopping_list.remove_list(list_id)
    return redirect(url_for("view_shopping_list"))

@app.route('/update_list/<list_id>', methods=['GET', 'POST'])
@is_logged_in
def update_list(list_id):
    """ Used to update a list""" 
    form = EditShoppingList(request.form)
    if request.method=='POST' and form.validate():
        list_name = form.list_name.data
        for shopping_id in Shopping_list.saved_lists:
            if shopping_id['list_id'] == list_id:
                shopping_id['list_name'] = list_name             
        return redirect(url_for('view_shopping_list'))
    return render_template('edit_shopping_list.html', saved_items= Shopping_list.saved_lists, form=form)



@app.route('/create_item/<list_id>', methods = ['GET', 'POST'])
@is_logged_in
def create_item(list_id):
    """ User can create and view their shopping list items"""
    form =  CreateShoppingItem(request.form)
    if request.method == 'POST' and form.validate():
        item_name = form.item_name.data
        new_item = Shopping_item(str(item_name), list_id)
        # new_item.shopping_item_store()
        new_item.create_shopping_item()
        print(Shopping_item.saved_items)
    return render_template('shopping_items.html', saved_items = Shopping_item.saved_items, form=form, list_id=list_id)

@app.route('/delete_item/<list_id>/<item_id>')
@is_logged_in
def delete_item(list_id, item_id):
    """ Link to do a delete method call"""
    Shopping_item.remove_item(item_id)  
    return redirect("/create_item/{}".format(list_id))

@app.route('/update_item/<list_id>/<item_id>', methods=['GET', 'POST'])
@is_logged_in
def update_item(list_id, item_id):
    """ Used to update an item""" 
    form = EditShoppingItem(request.form)
    if request.method=='POST' and form.validate():
        item_name = form.item_name.data
        for shopping_id in Shopping_item.saved_items:
            if shopping_id['list_id'] == list_id and shopping_id['item_id'] == item_id:
                shopping_id['item_name'] = item_name             
        return redirect('/create_item/{}'.format(list_id))
    return render_template('edit_shopping_item.html', saved_items= Shopping_item.saved_items, form=form, list_id=list_id)

@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))
