from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, legs):
        self._legs = legs
    def walk(self):
        print('walk')
    @abstractmethod
    def eat(self):
        pass