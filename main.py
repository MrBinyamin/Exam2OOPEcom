from Customer import Customer
from Gift import Gift
from Item import Item
from VipOrder import VipOrder

##my discount logic is precentage so you insert anumber between 0 to 1 for the disscount u want for example 0.25

item1=Item(101,"Laptop",1200.0)
item2=Item(102,"Mouse",25.0)
item3=Item(103,"Keyboard",75.0)

vip_customer=Customer(1,"ben","but","example","somwhere","VIP",0.25)

vip_order=VipOrder(500,"tech bundle","somwhereelse",[item1,item2],vip_customer,"CREDIT CARD")

print(f"VIp order total price= {vip_order.order_total_price}")
vip_customer.print_favorite()
vip_customer.add_item(item1)
vip_customer.print_favorite()
vip_customer.add_item(item3)
vip_customer.print_favorite()
vip_customer.remove_item(item3)

vip_customer.take_gift(Gift())
vip_customer.open_gift()

##check if without discount super woks as expected
regular_customer=Customer(2,"ben","but","example","somwhere","vip")
good_order=VipOrder(501,"Invalid","no",[item3],regular_customer,"CASH")

print(f"good order total price= {good_order.order_total_price}")


##error for  not vip customer to try and create vip order

regular_customer2=Customer(3,"ben","but","example","somwhere","regular")
bad_order=VipOrder(502,"Invalid","no",[item3],regular_customer2,"CASH")

