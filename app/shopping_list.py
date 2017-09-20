from uuid import uuid4
class Shopping_list(object):
    saved_lists=[]
    def __init__(self, list_name, list_id=None):
        """ Contains shopping list attributes required for Shopping list class """
        self.list_id = str(uuid4()) if list_id is None else list_id
        self.list_name = list_name

# new_li = Shopping_list("My Shopping")
# print('{} {}'.format(new_li.list_id, new_li.list_name))
    def shopping_list_store(self):
        new_shopping_list = {'list_id' : self.list_id,
                             'list_name': self.list_name}
        return new_shopping_list

    def create_shopping_list(self):
        """ Takes values stored as dict in shopping_list_store and appends to saved_lists """
        add_shopping_list = self.shopping_list_store()
        self.saved_lists.append(add_shopping_list)
        return add_shopping_list

    def view_lists(self):
        """ returns a list of all saved shopping lists"""
        return self.saved_lists
