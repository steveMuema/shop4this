[![Coverage Status](https://coveralls.io/repos/github/steveMuema/shop4this/badge.svg?branch=ch-test-coverage-reporting-%23151258154)](https://coveralls.io/github/steveMuema/shop4this?branch=ch-test-coverage-reporting-%23151258154)
[![Build Status](https://travis-ci.org/steveMuema/shop4this.svg?branch=ch-test-coverage-reporting-%23151258154)](https://travis-ci.org/steveMuema/shop4this)


# shop4this!
This allows users to record and share things they want to buy, meeting the needs of keeping track of the shopping lists

### Getting Started
Here is a step by step by guide on how to get the project running locally on a machine:
* Clone this repository to your local terminal using https://github.com/steveMuema/shop4this.git link to your      github account.
* Run the application locally on your terminal by 
> cd /path/to/shop4this then http://127.0.0.1:5000/ to run on your browser
> write python run.py to run the application
* Run tests locally by 
> nosetests tests/ 

### Prerequisites
Install the following softwares for the application to run locally:
* Pipenv or virtualenvwrapper for setting up your environment variables.
    * **pip install pipenv** on your bash terminal to install.
    * run **pipenv shell** to activate the environment.
* Install Flask.
    * run **pip install flask** command to your terminal to install.
    * run **FLASK_APP=run.py flask run** to start the application.

### Installing
Here is a procedure on how to get a development environment running:
* After installing pipenv, you can run the command **pipenv shell** to activate your environment. 
* To run the application for development, run the command **python run.py** inside your path/to/shop4this directory.

### Deployment
This application can be deployed to a live system by:
> * pip install heroku on your bash terminal
> * run the command heroku login to login to your account
> * run heroku create command to create the live system
> * Go to https://herokuapp.com to setup and deploy your application in the dashboard.
> * Open app on your dash board after successful deployment.

### Built With
* Maven-For designs of the wireframes.
* Flask-The web framework used.

### Authors
* **Steve Muema**

### Acknowledgments
* Andela Community for the support during the process of creating this application 

