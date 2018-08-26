from uuid import uuid4
class Shopping_list(object):
    saved_lists=[]
    def __init__(self, list_name, list_id=None):
        """ Contains shopping list attributes required for Shopping list class """
        self.list_id = str(uuid4()) if list_id is None else list_id
        self.list_name = list_name

    def shopping_list_store(self):
        """ Stores list in a dictionary and returns result """
        new_shopping_list = {'list_id' : self.list_id,
                             'list_name': self.list_name}
        return new_shopping_list

    def create_shopping_list(self):
        """ Takes values stored as dictionary and appends to saved_lists """
        add_shopping_list = self.shopping_list_store()
        self.saved_lists.append(add_shopping_list)
        return add_shopping_list

    def view_lists(self):
        """ returns a list of all saved shopping lists"""
        return self.saved_lists

    @staticmethod
    def remove_list(list_id):
        """ method to remove specific shopping list"""
        selected_list = [shop_list for shop_list in Shopping_list.saved_lists if list_id == shop_list['list_id']]
        # print(selected_list)
        Shopping_list.saved_lists.remove(selected_list[0])
        return True

    def update_list(self, list_name, list_id):
        """ method for updating the Shopping list """
        for list_id in saved_lists:
            self.list_name = list_name
            self.list_id = list_id
        return self

