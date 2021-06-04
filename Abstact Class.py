#Abstract class
# solution for 1 &2
from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
    def show(self):
        print("It takes some time to run")
class Laptop(Computer):
    def process(self):
        print("its running")
# com = Computer()
com1 = Laptop()
com1.process()
com1.show()







#solution for 3 and 4
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
    def display(self):
        print("move")
class Human(Animal):
    def move(self):
        print(" Human : I can walk and run")
class Snake(Human):
    def move(self):
        print("Snake : I can crawl")
    def walk(self):
        print("snake : I cannot walk")
class Dog(Snake):
    def move(self):
        print("dog : I can bark")
H = Human()
S = Snake()
D= Dog()
H.move()
S.move()
D.move()
D.display()
# D.walk()