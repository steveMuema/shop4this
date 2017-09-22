import unittest
from app.models.user import User
class TddForUserClass(unittest.TestCase):
    """ Tests all implemented methods for accessing user class """
    def setUp(self):
        """ set up object for User class to be tested"""
        self.user = User('Steve Muema', 'stevemuema@gmail.com','say123#')
    def test_compare_password(self):
        """test whether password inputs are equal before user creates account"""
        validate_password = self.user.password 
        self.assertEqual('say123#', validate_password)   
    def test_registration_store(self):
        """ tests whether the user dictionary is saved in user_list"""
        add_user = self.user.registration_store()
        self.assertEqual([add_user], User.user_list)

    def test_successful_signin(self):
        """ tests whether the sign in attempt was successful"""
        login_user = User.signin(self.user.email, self.user.password)
        self.assertEquals("Successfully signed in", login_user)

if __name__ == "__main__":
    unittest.main()