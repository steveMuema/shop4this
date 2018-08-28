from uuid import uuid4
import json
class User(object):
    user_list=[]
    def __init__(self, username, email, password,  user_id=None, phone_no=None, business_no=None ):
        self.user_id = str(uuid4()) if user_id is None else user_id 
        self.username = username 
        self.email = email
        self.password = password
        self.phone_no = phone_no if phone_no is None else phone_no
        self.business_no =business_no if business_no is None else business_no
        
       

    def registration_store(self):
        """ method to register user credentials in a list"""
        user_validation = self.email_exists()
        if user_validation is False:
            user_credentials = {'user_id' : self.user_id,
                                'username': self.username,
                                'email': self.email,
                                'password': self.password,
                                'phone_no': self.phone_no, 
                                'business_no': self.business_no}
            with open("user_data_dumps.json", "w") as write_file:
                 return json.dump(user_credentials, write_file)
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
        # auth_user = User.user_list
        auth_email = [account_email['email'] for account_email in User.user_list if email is account_email['email']]
        auth_pswd = [ account_pswd['password'] for account_pswd in User.user_list if password is account_pswd['password'] ]
        auth_account=(auth_email, auth_pswd)     
        auth_input = ([email], [password])
        print(auth_account, auth_input)
        if auth_account == auth_input:
            return "Successfully signed in"
        else:
            return False