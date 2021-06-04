
#Interfaces
import zope.interface as interface
class Lunch(interface.Interface):
    northindian = interface.Attribute("choci")
    def food(self,northindian):
        pass
@interface.implementer(Lunch)
class A(interface.Interface):
    def food(self,northindian):
        return northindian

obj = A['food']
print(obj)








#Interface with 2 methods (2&3)solution
import zope.interface as interface
class Lunch(interface.Interface):
    northindian = interface.Attribute("choci")
    def food(self,northindian):
        pass
    def coldrinks(self,beverages):
        pass
@interface.implementer(Lunch)
class A(interface.Interface):
    def food(self,northindian):
        return northindian

food = Lunch['food']
print(Lunch.implementedBy(A))








# interface inherits interface
import zope.interface as interface
class A(interface.Interface):
    def m1(self,x):
        pass
    def m2(self):
        pass
class B(A):
    def m3(self,x,y):
        pass
@interface.implementer(B)
class C:
    def m1(self,z):
        return z**3
    def m2(self):
        return 'hi'
    def m3(self,x,y):
        return x^y
print(A.implementedBy(C))
print(B.implementedBy(C))
print(A.isEqualOrExtendedBy(B))
print(B.isOrExtends(B))








#interface with public private and protected method
import zope.interface as interface
class Lunch(interface.Interface):
    northindian = interface.Attribute("choci")
    def food(self,northindian):
        pass
    def _coldrinks(self,_beverages):
        pass
    def __dinner(self):
        pass
@interface.implementer(Lunch)
class A:
    def food(self,northindian):
        return northindian
    def _coldrinks(self,beverages):
        return beverages
    def __dinner(self):
        return 'x'
obj = A()
print(Lunch.implementedBy(A))

