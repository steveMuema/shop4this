from uuid import uuid4
import json
class User(object):
    def __init__(self, username, email, password,  user_id=None, phone_no=None, business_no=None ):
        self.user_id = str(uuid4()) if user_id is None else user_id 
        self.username = username 
        self.email = email
        self.password = password
        self.phone_no = phone_no if phone_no is None else phone_no
        self.business_no =business_no if business_no is None else business_no
        
       

    def registration_store(self):
        """ method to register user credentials in a json file permanently """
        user_credentials = {'user_id' : self.user_id,
                            'username': self.username,
                            'email': self.email,
                            'password': self.password,
                            'phone_no': self.phone_no, 
                            'business_no': self.business_no}
        with open("user_data_dumps.json", "w") as write_file:
            return json.dump(user_credentials, write_file)