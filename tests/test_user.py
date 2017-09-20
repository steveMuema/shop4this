import unittest
from app.user import User
class TddForUserClass(unittest.TestCase):
    # def setUp(self):
    #     """ set up object for User class to be tested"""
    #     self.user = User('Steve Muema', 'stevemuema@gmail.com','say123#', "say123#")

    def test_compare_password(self):
        """test whether password inputs are equal before user creates account"""
        user= User('Steve Muema', 'stevemuema@gmail.com','say123#', "say123#")
        validate_password= user.compare_password()  
        self.assertEqual("say123#", validate_password)
    
    def test_registration_store(self):
        """ tests whether the user dictionary is saved in user_list"""
        user= User('Steve Muema', 'stevemuema@gmail.com','say123#', "say123#")
        self.assertListEqual([user.registration_store()], User.user_list)
    def test_signin(self):
        user= User('Steve Muema', 'stevemuema@gmail.com','say123#', "say123#")        
        User.registration_store(user)
        user_login = self.signin("stevemuema27@gmail.com", 'say123#')

if __name__ == "__main__":
    unittest.main()