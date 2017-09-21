""" Sets the app to intergrate Flask"""
from flask import Flask



#initialize the app
app = Flask(__name__, instance_relative_config=True)

#load the views
from app import views

