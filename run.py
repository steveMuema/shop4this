""" This module is used for importing app module and run it if the __name__ == '__main__'
    Run this file to start server side rendering of web application"""

from app import app
if __name__ == "__main__":
    app.run(debug=True)