import unittest
from app.models.shopping_item import Shopping_item

class TddForShoppingItem(unittest.TestCase):
    def setUp(self):
        self.shopping_item = Shopping_item("My Shopping item", "123")

    def test_create_shopping_item(self):
        """ tests the shopping items if it is appended to the saved_items"""
        saved_shopping_item = self.shopping_item.create_shopping_item()
        self.assertEqual([saved_shopping_item], self.shopping_item.saved_items)

    def test_view_item(self):
        """test if method returns a list,saved_items, that stores all shopping items """
        view_items = self.shopping_item.view_items()
        all_items = Shopping_item.saved_items 
        self.assertEqual(all_items, view_items)

    def test_remove_item(self):
        """ tests for removal of a shopping items """
        select_item = self.shopping_item.create_shopping_item() 
        remove_selected = self.shopping_item.remove_item(select_item['item_id'])
        self.assertEqual(True, remove_selected)
