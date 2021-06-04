#2 methods wid same name but diff no of parameters
from multipledispatch import dispatch
@dispatch(int,int)
def product(a,b):
    r=a*b
    print(r)
@dispatch(int,int,int)
def product(a,b,c):
    r=a*b*c
    print(r)
product(1,2)
product(2,3,4)







#2 methods wid same name but diff no of parameters of diff datatype
from multipledispatch import dispatch
@dispatch(int,int)
def product(a,b):
    r=a+b
    print(r)
@dispatch(float,float,float)
def product(a,b,c):
    r=a+b+c
    print(r)
product(2,3)
product(1.1,3.3,4.0)








#2 methods wid same name but diff no of parameters of same datatype
from multipledispatch import dispatch
@dispatch(int,int)
def product(a,b):
    r=a*b
    print(r)
@dispatch(int,int)
def product(a,b):
    r=a*b
    print(r)
product(1,2)
product(2,3)








#2 method with same name but different return type
from multipledispatch import dispatch
@dispatch(int,int)
def product(a,b):
    return str(a*b)
@dispatch(int,int)
def product(a,b):
    return str(a*b)

b=product(1,2)
a=product(2,3)
print(b)
print(a)
print(type(a))
print(type(b))


