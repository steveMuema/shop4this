import unittest
from app.models.shopping_list import Shopping_list

class TddForShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = Shopping_list("My Shopping list")

    def test_create_shopping_list(self):
        """ tests the shopping lists if it is appended to the saved_lists"""
        saved_shopping_list = self.shopping_list.create_shopping_list()
        self.assertEqual([saved_shopping_list], self.shopping_list.saved_lists)

    def test_view_list(self):
        """test if method returns a list,saved_lists, that stores all shopping lists """
        view_lists = self.shopping_list.view_lists()
        all_lists = Shopping_list.saved_lists 
        self.assertEqual(all_lists, view_lists)

    def test_remove_list(self):
        """ tests for removal of a shopping list """
        select_list = self.shopping_list.create_shopping_list() 
        remove_selected = self.shopping_list.remove_list(select_list['list_id'])
        self.assertEqual(True, remove_selected)
