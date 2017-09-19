import unittest
from app.user import User
class TddForUserClass(unittest.TestCase):
    def setUp(self):
        """ set up object for User class to be tested"""
        self.user = User()

    def test_compare_password(self):
        """test whether password inputs are equal before user creates account"""
        result = self.user.compare_password("say123#", "say123#")
        self.assertEqual("say123#", result)

if __name__ == "__main__":
    unittest.main()