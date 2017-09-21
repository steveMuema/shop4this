from flask import Flask, render_template, request
from app import app

@app.route('/register')
def register():
    """ Returns the register UI. """
    return render_template("signup.html")

@app.route('/login')
def login():
    return render_template("signin.html")

@app.route('/shopping-list')
def view_shopping_list():
    return render_template("shopping_list.html")

@app.route('/shopping-item')
def view_shopping_item():
    return render_template("shopping_items.html")
