#Exception Handling
# Arithmetic Exception using try-except
try:
    a = 10/0
    print(a)
except ArithmeticError:
    print("The statement is raising arithmetic exception")

else:
    print("Success")










#throw an exception with your own message
#class A(Exception):
#   pass
#x=-1
#if x<0:
#    raise Exception("sorry, no numbers below zero")








#Multiple exception blocks
a,b=1,0
try:
    print(a/b)
    print("this wont be printed")
    print('10'+10)
except TypeError:
    print("values cannot be added")
except ZeroDivisionError:
    print("Sorry!,num cannot be devided by zero")










#pgm to create own exception
class MyException(Exception):
    def __init__(self,message):
        self.message = message

try:
    raise MyException("Something is Fishy")
except MyException as err:
    print("Message :",err.message)











#pgm with finally block
a=5
b=0
try:
    print("resource open")
    print(a/b)
except Exception:
    print("You cannot devide a number by zero")
finally:
    print("resource closed")

# indexError exception in python
try:
    a=['a','b','c']
    print(a[4])

except LookupError:
    print("index Error  Exception raised,list index out of range")
else:
    print("Success, No error")













#FileNotFound Exception

try:
    f = open("somefile.txt",'r')
    print(f.read)
    f.close()
except FileNotFoundError:
        print("wrong file or path")

# IO error
try:
    f = open("somefile.txt",'r')
    print(f.read)
    f.close()
except IOError:
    print("wrong file or path")













#string index out of range
string = "123456"
try:
    str=string[8]
    print(str)
except IndexError:
    print("Exception: Index out of range")
