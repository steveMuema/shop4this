""" Sets the app to intergrate Flask"""
from flask import Flask
from flask_bootstrap import Bootstrap



#initialize the app
app = Flask(__name__, instance_relative_config=True)
Bootstrap(app)

#  we also hard-code disabling the CDN support
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
#load the views
from app import views

