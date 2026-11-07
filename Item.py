class Item:
    def __init__(self,id ,name,price):
        self.id = id
        self.name = name
        self.price = price
    def __eq__(self, other):
        return self.name == other.name