from uuid import uuid4
class User(object):
    def __init__(self, username, email, password, confirm_password, user_id=None):
        self.user_id = uuid4() if user_id is None else user_id 
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

# user = User('Steve Muema', 'stevemuema@gmail.com','say123#', "say123#")
# print('{}, {}'.format(user.user_id, user.username))
    def compare_password(self):
        return '{} {}'.format(self.password, self.confirm_password)

user = User('Steve Muema', 'stevemuema@gmail.com','say123#', "say123#")
print(User.compare_password(user))
        
           
                
