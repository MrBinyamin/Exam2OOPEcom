from Order import Order


class VipOrder(Order):



    def total_price(self):
        if self.order_customer.customer_type!="VIP":
            raise Exception("Customer type is not VIP but tried to create an VIP order")
        if self.order_customer.customer_discount is not None:
            temp_discount=1-self.order_customer.customer_discount
            sum=0
            for i in self.items:
                sum+=i.price
            return sum*temp_discount
        else:
            return super().total_price()