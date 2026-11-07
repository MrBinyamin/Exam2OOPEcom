from bonus.Animal import Animal
from bonus.Pet import Pet


class Fish(Animal,Pet):
    def __init__(self):
        super().__init__(0)
        self.name = ""
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def play(self):
        print("the fish plays?")
    def walk(self):
        print("the fish walks?")
    def eat(self):
        print("the fish eats!")