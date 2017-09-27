from flask import Flask, render_template, request,url_for, redirect
from app.my_app import app
from app.controller import RegisterForm, CreateShoppingList, LoginForm, CreateShoppingItem
from app.models.user import User
from app.models.shopping_list import Shopping_list
from app.models.shopping_item import Shopping_item
from flask_login import login_user, login_required

app.config['SECRET_KEY']  = 'itsmysecret'

@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Returns the register UI. """
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.password.data
        new_user = User(str(username), str(email), str(password))
        if  User.email_exists(new_user):
            error="Account exists. Sign in to the account"
            return render_template("signup.html", error=error)
        new_user.registration_store()
        # login_user(new_user)
        return redirect(url_for('login'))       
    return render_template("signup.html", form= form)

@app.route('/login', methods = ['GET', 'POST'])
# @login_required
def login():
    """ Enable user to login his her credentia;s """
    all_users = User.user_list
    form = LoginForm(request.form)
    if request.method=='POST':
        email = form.email.data
        password = form.password.data
        auth_email = [account_email['email'] for account_email in all_users ]
        auth_pswd = [ account_pswd['password'] for account_pswd in all_users  ]
        auth_account=(auth_email, auth_pswd)     
        auth_input = ([str(email)], [str(password)])
        if auth_account != auth_input:
            error = "Login unsuccessful. Please retry "
            return render_template("signin.html",form=form, error=error)
                        
        return redirect(url_for('view_shopping_list'))
    return render_template("signin.html", form = form)

@app.route('/shopping_list', methods=['GET', 'POST'])
# @login_required
def view_shopping_list():
    """" User can create and view their shopping lists """
    form = CreateShoppingList(request.form)
    if request.method == 'POST' and form.validate():
        list_name = form.list_name.data
        new_list = Shopping_list(list_name)
        new_list.shopping_list_store()
        new_list.create_shopping_list()
    return render_template("shopping_list.html", saved_lists= Shopping_list.saved_lists, form=form)


@app.route('/delete_list/<list_id>')
# @login_required
def delete_list(list_id):
    """ Link to do a delete method call"""
    Shopping_list.remove_list(list_id)
    return redirect(url_for("view_shopping_list"))

@app.route('/update_list/<list_id>', methods=['GET', 'POST'])
# @login_required
def update_list(list_id):
    """ Used to update a list""" 
    form = CreateShoppingList(request.form)
    if request.method=='POST' and form.validate():
        list_name = form.list_name.data
        selected_list = Shopping_list(list_name)
        selected_list.update_list(list_name, list_id)



@app.route('/create_item/<list_id>', methods = ['GET', 'POST'])
# @login_required
def create_item(list_id):
    """ User can create and view their shopping list items"""
    form =  CreateShoppingItem(request.form)
    if request.method == 'POST' and form.validate():
        item_name = form.item_name.data
        new_item = Shopping_item(str(item_name), list_id)
        # new_item.shopping_item_store()
        new_item.create_shopping_item()
    return render_template('shopping_items.html', saved_items = Shopping_item.saved_items, form=form, list_id=list_id)

@app.route('/delete_item/<list_id>/<item_id>')
# @login_required
def delete_item(list_id, item_id):
    """ Link to do a delete method call"""
    # if request.method=='POST':
    Shopping_item.remove_item(item_id)  
    return redirect("/create_item/{}".format(list_id))
    # return render_template('shopping_items.html',  saved_items = Shopping_item.saved_items, list_id=list_id)

