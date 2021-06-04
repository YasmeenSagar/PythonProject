#STATIC
#class with static var, instance var, static method and instance method
class Student:
    school = "Telusko"                  #static variable
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2                    #instance variables
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):                       #accessor method
        return self.m1
    def set_m1(self,values):                #mutator method
        self.m1=values

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def infor():
        print("This is Students class")

c1=Student(34,42,63)
c2=Student(89,32,12)

print(c1.avg())
print(c2.avg())
print(c1.get_m1())
print(Student.info())
Student.infor()







#Print instance var in static method

class Car:
    wheels = 4
    def __init__(self,com,mil):
        self.com = com
        self.mil = mil

        @staticmethod
        def info():
            print(f"car is {self.com}")
            print(f"mil is {self.mil}")
c1=Car("BMW",10)
c2 = Car("Benz",20)
print(c1.com,c1.mil)
print(c2.com,c2.mil)






#print static var inside  the instance method
class Test:
    a=10
    def __init__(self):
        print(self.a)
    def method(self):
        print(self.a)
        print(Test.a)

t=Test()
t.method()






#Call instant in static method
class MyClass:
    def __init__(self):
        self.data = "hii"
    def method(self):
        print("instance method called with instance",(self.data))

    @staticmethod
    def static_method(data):
        print("Static method called with data",(data))

c = MyClass()
c.method()
c.static_method("hello")






# call static method in instance method
class Music:
    @staticmethod
    def play():
        print("play music from static method")

    def stop(self):
        # print("stop playing")
        self.play()
        Music.play()
c = Music()
c.stop()
