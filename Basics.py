#BASICS
#class,object,method
from inspect import signature
class Details:  #creating class
    def __init__(self):
        self.name="harry"
        self.age=22

    def info(self):  #method
        print(f"name of a person is {self.name}")
        print(f"age of that person is {self.age}")


d=Details()  #class object
d.info()










# program to print my name
name = input("Enter your name: ")
print(f"Hello {name}")







# single ,multi line and documentation comments

# print("Hello World")    #printing a string (single line comment)




# It is a
# Multiline
# comment

def func(a,b):
    """
This is
Doc String
"""
    return a+b
func(2,3)










# variables for different data types

a= 123
print(type(a))

b="123"
print(type(b))

c=4.5
print(type(c))

d= 2+3j
print(type(d))

e=5>4
print(type(e))














# local and global variables
a=10        #global variable
def abd():
    global a
    a=15            #local variable
    print(a)
abd()
# print(a)









# function to print name and call the function from main
def main():
    print("tom")
if __name__=="__main__":
    main()
# print("tom")

name=input("Enter your name :")
def info(name):
    print("my name is",name)

info(name)
#


