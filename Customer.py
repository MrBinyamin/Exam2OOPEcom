
from typing import Optional
import Gift



class Customer:

    _existing_customer_ids=set()

    def __init__(self, id, first_name, last_name, email, delivery_address, customer_type, customer_discount:Optional[float]=None):
        if id in self._existing_customer_ids:
            raise Exception("the customer id is already exisitng")
        self._existing_customer_ids.add(id)
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.customer_type = customer_type.upper()
        self.customer_discount = customer_discount
        self.favorite_items = []
        self.customer_gift = None

    def update_favorite(self,items):
        for i in items:
            self.add_item(i)

    def print_favorite(self):
        print("the following items are in favorite list:")
        for item in self.favorite_items:
            print(f"item ID {item.id} and item name is: {item.name}")

    def remove_item(self,item):
           self.favorite_items.remove(item)

    def add_item(self,item):
        if item not in self.favorite_items:
            self.favorite_items.append(item)

    def take_gift(self,gift:Gift):
        self.customer_gift=gift

    def open_gift(self):
        if self.customer_gift:
            self.customer_gift.open()
        else:
            print("no gift to open")