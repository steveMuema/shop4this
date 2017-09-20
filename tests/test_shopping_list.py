import unittest
from app.shopping_list import Shopping_list

class TddForShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = Shopping_list("My Shopping list")

    def test_create_shopping_list(self):
        """ tests the shopping lists if it is appended to the saved_lists"""
        saved_shopping_list = self.shopping_list.create_shopping_list()
        self.assertEqual(self.shopping_list.view_lists(), [saved_shopping_list])

    def test_view_list(self):
        """test if method returns a list,saved_lists, that stores all shopping lists """
        all_shopping_lists = self.shopping_list.view_lists()
        self.assertEqual(Shopping_list.saved_lists, all_shopping_lists)