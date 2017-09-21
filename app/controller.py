from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField
from wtforms.validators import InputRequired, Email, Length

class RegisterForm(Form):
    """ form that handles registration"""
    username = StringField('Username', [validators.Length(min=4, max=25),
            validators.InputRequired(message="Please provide your name"),
            validators.DataRequired(message="Empty username field. Please provide valid username")])
    email = StringField('email', [validators.Length(min=6, max=50),
            validators.Email(message="Please enter a valid address"), validators.InputRequired(message="Please provide email"),
            validators.DataRequired(message="Empty email field. Please provide valid email address")])
    password = PasswordField('password', [
        validators.DataRequired(message="Please enter a password"),
        validators.Length(min=8, max=25, message="passwords must be more than 8 characters"),
        validators.EqualTo('confirm', message='Passwords do not match'),
        validators.InputRequired(message="Please provide a strong password")
    ])
    confirm_password = PasswordField('Confirm Password', [
        validators.DataRequired(message="Please re-enter password"),
        validators.Length(min=8, max=25, message="passwords must be more than 8 characters"),
        validators.InputRequired(message="This field is required")
    ])
class LoginForm(Form):
    """ form that handles login"""
    email =  StringField('email', validators=[InputRequired(), Length(min=4, max=25)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=25)])

class CreateShoppingList(Form):
    """ handles new buckets created"""    
    list_name = StringField('list_name', validators=[InputRequired(), Length(min=4, max=140)])

class CreateShoppingItem(Form):
    """ used to create new activity"""
    item_name = StringField('item_name', validators=[InputRequired(), Length(min=4, max=140)])
   
class EditShoppingList(Form):
    """  edits available buckets """
    list_name = StringField('list_name', validators=[InputRequired(), Length(min=4, max=140)])

class EditShoppingItem(Form):
    """ edits available activity"""
    item_name = StringField('list_name', validators=[InputRequired(), Length(min=4, max=140)])
