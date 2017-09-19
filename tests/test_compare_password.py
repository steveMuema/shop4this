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
        self.assertIn("say123#", validate_password)

if __name__ == "__main__":
    unittest.main()