from uuid import uuid4
from app.models.shopping_list import Shopping_list
class Shopping_item(object):
    saved_items=[]
    def __init__(self, item_name, list_id, item_id=None):
        """ Contains shopping item attributes required for Shopping item class """
        self.item_id = str(uuid4()) if item_id is None else item_id
        self.item_name = item_name
        self.list_id = list_id

    # def shopping_item_store(self):
    #     """ saves the shopping items in dict and returns result"""
    #     new_shopping_item = {'item_id' : self.item_id,
    #                          'item_name': self.item_name,
    #                          'list_id': self.list_id}
    #     return new_shopping_item

    def create_shopping_item(self):
        """ Takes values stored as dictionary and appends to saved_items """
        add_shopping_item = {'item_id' : self.item_id,
                             'item_name': self.item_name,
                             'list_id': self.list_id}
        self.saved_items.append(add_shopping_item)
        return add_shopping_item

    def view_items(self):
        """ returns a list of all saved shopping items"""
        return self.saved_items

    @staticmethod
    def remove_item(item_id):
        """ method to remove specific shopping item"""
        selected_item = [shop_item for shop_item in Shopping_item.saved_items if item_id == shop_item['item_id']]
        Shopping_item.saved_items.remove(selected_item[0])
        return True

    def update_item(self, item_name, item_id):
        """ method for updating the Shopping items """
        self.item_name = item_name
        self.item_id = item_id
        return self

# new_item = Shopping_item("my item", "1234")
# new_item.create_shopping_item()
# print(new_item.create_shopping_item())