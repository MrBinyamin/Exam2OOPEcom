from bonus.Animal import Animal
from bonus.Pet import Pet


class Cat(Animal,Pet):
    def __init__(self,name:str =""):
        super().__init__(4)
        self.name = name
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def play(self):
        print("the cat plays")
    def eat(self):
        print("the cat eats")