from uuid import uuid4
import json
class MyProduct(object):
    def __init__(self, product_name, product_price, product_id=None):
        """ Contains shopping list attributes required for Shopping list class """
        self.product_id = str(uuid4()) if product_id is None else product_id
        self.product_name = product_name
        self.product_price = product_price

    def my_products_store(self):
        """ Stores list in a dictionary and returns result """
        new_product = {'product_id' : self.product_id,
                             'product_name': self.product_name, 
                             'product_price': self.product_price,}
        with open("products_data_dumps.json", "w") as writefile:
            return json.dumps(new_product, writefile)

    

