# ACCESS MODIFIERS
#create cls with private access modifier and try to access it from another class
class Student:
    def __init__(self,name,roll,branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    def __displayDetails(self):
        print("Name:",self.__name)
        print("Roll:",self.__roll)
        print("Branch:",self.__branch)
    def accessPrivateFunction(self):
        self.__displayDetails()
# # obj = Student("abc",20,"EC")
# # obj.accessPrivateFunction()
# # obj.__displayDetails()         #displaying error
# # obj._Student__displayD
class A(Student):
    def __init__(self,name,roll,branch):
        super().__init__(name,roll,branch)
    def PrivateFunction(self):
        self.accessPrivateFunction()
obj = A("abc",20,"EC")
obj.PrivateFunction()





#Protected modifier in the same
class A:
    def __init__(self,name,roll):
        self._name = name
        self._roll = roll

    def _show(self):
        print("Name:", self._name)
        # print("Roll:", self._roll)

class B(A):
    def __init__(self,name,roll):
    #         # super().__init__(name,roll)
        super().__init__(name,roll)

    def showB(self):
        print("Roll:", self._roll)
        self._show()
c=B("abc",20)
c.showB()







#Access Protected method from child class in different module
class Computer:
    def __init__(self,brand,cpu):
        self._brand =brand
        self._cpu = cpu
    def _display(self):
        print("Brand:",self._brand)






#Access the public method from any class in same module
class A:
    def __init__(self):
        print("this is init of A")
    def show(self):
        print("This is class A")

class B(A):
    def __init__(self):
        super().__init__()
    def display(self):
        self.show()
obj = B()
obj.display()
