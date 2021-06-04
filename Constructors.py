#CONSTRUCTORS
# Default constructor
class A:
    def __init__(self):
        self.a="name"

    def print_a(self):
        print(self.a)

obj = A()
obj.print_a()





#a constructor with 2 arguements
class A:
    def __init__(self,b,c):
        self.b = b
        self.c = c
    def print_arg(self):
        print(self.b)
        print(self.c)

obj = A("name","age")
obj.print_arg()













#call default and arg constructor of super classrm child
class Parent:
    def __init__(self,x):
        print(x)
class Child(Parent):
    def __init__(self,x):
        super().__init__(x)
b=Child("age")












#private protected and public access modifiers

class A:
    def __init__(self,v1,v2,v3):
        self.v1 = v1
        self._v2 = v2
        self.__v3 = v3
    def publicmethod(self):
        print("public data member :",self.v1)

    def _protectedmethod(self):
        print("protected data member:",self._v2)
    def __privatemethod(self):
        print("private data member:",self.__v3)

    def displayPrivate(self):
        self.__privatemethod()

class B(A):
    def __init__(self,v1,v2,v3):
        super().__init__(v1,v2,v3)

    def displayProtected(self):
        self._protectedmethod()
obj = B("a",6,"b")
obj.publicmethod()
obj.displayProtected()
obj.displayPrivate()








#Constructor with return type int and string
"""
not possible to return int or string type by costructor
class A:
    def __init__(self,a,b):
         return 4
         return "abc"
c= A(4,"abc")
"""

""" It is not possible to call the constructor twice"""