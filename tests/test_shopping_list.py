import unittest
from app.shopping_list import Shopping_list

class TddForShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = Shopping_list("My Shopping list")
    def test_view_list(self):
        """test if method returns a list,saved_lists, that stores all shopping lists """
        all_shopping_lists = self.shopping_list.view_lists()
        print("All shopping lists are stored here")
        self.assertEqual([], all_shopping_lists)