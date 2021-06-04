# LOOPS


#program to print "Bright IT Career" ten times using for loop

for i in range(11):
    print(f"Bright IT Careers {i}")



#Program to print 1-20 nums using while loop
i=1
while i<=20:
    print(i)
    i=i+1



# Program for equal and not equal to operators

a= 20
b= 3
print(a==b)
print(a!=b)




#Program for odd and even numbers
list = [1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for i in list:
    if (i%2)==0:
        even.append(i)
    else:
        odd.append(i)
print("list of odd number is :",odd)
print("list of even number is :",even)




# Program to find largest among three numbers
def largest(num1,num2,num3):
    if num1>num2:
        f1 = num1
    else:
        f1= num2

    if num2>num3:
        f2= num2
    else:
        f2= num3

    if f1>f2:
        print(f"{f1} is largest")
    else:
        print(f"{f2} is largest")
largest(55,90,10)





#pgm to find even num between 10 to 100 using while

i=10
while i<=100:
    if i%2==0:
        print(i)
    i=i+1

#Print 1-10 using do while
#python does not have a do while loop
i=1
while True:
    print(i)
    i=i+1
    if i>10:
        break




#Pgm to find armstrong num or not

num= int(input("Enter a number :"))
i=num
result=0
n=len(str(i))
while i!=0:
    digit = i%10
    result = result+ digit**n
    i=i//10
if num == result:
    print(num,"is armstrong")

else:
    print(num,"is not armstrong")




# program to find prime or not

num = int(input("Enter a num :"))
prime = True
for i in range(2,num):
    if num%i==0:
        prime = False
    break

if prime:
    print("number is prime ")
else:
    print("number is not prime")




#program to find palindrome or not
num = int(input("Enter a number :"))
temp = num
rev = 0
while num>0 :
    dig = num%10
    rev = rev*10+dig
    num = num//10

if temp == rev:
    print(temp,"is palindrome")
else:
    print(temp,"is not palindrome")




#pgm to find given number is even or odd
num = int(input("Enter a num :"))
if num%2==0:
    print("Even number")
else:
    print("Odd number")




#program to print gender male or female
gender = input("Enter your gender in (M/F) :")
if gender == 'M':
    print("Male")
elif gender=='F':
    print("Female")
else:
    print("Unspecified gender")




#pgm to find largest im 10,20 and 30
def max(num1,num2,num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3

    else:
        if (num2>num3):
            return num2
        else:
            return num3

m= max(10,20,30)
print("the largest num is" ,m)
