#OPERATORS
# function for arithmetic operators

a=6
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)




# function for ++ and __
a=4
'''print(a++)
throws error because this operator is not supported in python
'''
a+=1
print(a)

a-=1
print(a)




# program to find the 2 numbers are equal or not

num1= int(input("Enter the 1st number:\n"))
num2= int(input("Enter the 2nd number:\n"))
if num1==num2:
    print("numbers are equal")
else:
    print("numbers are not equal")




# program on logical and ,or,not

x= True
y=False
print(x and y)
print(x or y)
print(not x)



# program for relational operators

x=10
y=12
print(x>y)
print(x<y)
print(x==y)
print(x>=y)
print(x<=y)
print(x!=y)




#smaller and larger number

lst= []
num = int(input("how many numbers: "))
for i in range(num):
    nums=int(input("Enter numbers : "))
    lst.append(nums)

print(f"Large number is {max(lst)} ")
print(f"smaller number is {min(lst)}")
