from uuid import uuid4
class User(object):
    user_list=[]
    def __init__(self, email, password, confirm_password, username, user_id=None):
        self.user_id = str(uuid4()) if user_id is None else user_id 
        self.username = username 
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

# user = User('Steve Muema', 'stevemuema@gmail.com','say123#', "say123#")
# print('{}, {}'.format(user.user_id, user.username))
    def compare_password(self):
        if self.password is self.confirm_password:
            return '{}'.format(self.password)
        else:
            return "The passwords do not match."

    def registration_store(self):
        """ method to register user credentials in a list"""
        user_validation = self.email_exists()
        if user_validation is False:
            # return "Account exists. Sign in to the account", self.email 
            user_credentials = {'user_id' : self.user_id,
                                'username': self.username,
                                'email': self.email,
                                'password': self.password,}
            self.user_list.append(user_credentials)
            return user_credentials   
        else:
            return user_validation
    
    def email_exists(self):
        """ validates whether there is an existing email before creating a new account """
        all_mails = [exists['email'] for exists in User.user_list if self.email == exists['email']]
        if self.email in all_mails:
            return "Account exists. Sign in to the account"+', '+ str(self.email)            
        else:
            return False
    
    @staticmethod
    def signin(email, password):
        auth_email = [account_email['email'] for account_email in User.user_list if email is account_email['email']]
       
        auth_pswd = [ account_pswd['password'] for account_pswd in User.user_list if password is account_pswd['password'] ]
        auth_account=(auth_email, auth_pswd)
        auth_input = ([email], [password])
        if auth_account == auth_input:
            return "Successfully signed in"
        else:
            return False
       
    
