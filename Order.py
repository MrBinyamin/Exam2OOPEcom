from datetime import datetime
from typing import Optional
from Customer import Customer
from Item import Item


class Order:
    _existing_order_ids=set()
    def __init__(self,id,name:str,delivery_address:str,items:list[Item],order_customer: Customer,payment_method,order_date:Optional[datetime]=None):
        if id in self._existing_order_ids:
            raise Exception("Order id is already in use")
        self._existing_order_ids.add(id)
        self.id = id
        self.name = name
        self.delivery_address = delivery_address
        self.items = items
        self.order_customer = order_customer
        self.payment_method = payment_method
        self.order_date = order_date or datetime.now()
        self.order_total_price = self.total_price()
        self.order_customer.update_favorite(items)
    def total_price(self):
        sum=0
        for i in self.items:
            sum += i.price
        return sum