
from AccessModifiers import *
class Laptop(Computer):
    def __init__(self,brand,cpu):
        super().__init__(brand,cpu)
    def show(self):
        print("cpu :",self._cpu)
        self._display()
o=Laptop("hp","i5")
o.show()

