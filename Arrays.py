#ARRAYS

#Function to add integer values of array
from array import *
a = array('i',[1,2,3,4,5])
sum = 0
for i in range(len(a)):
    sum = sum+a[i]
print("the sum of integers is ",sum)





#Function to find avg value of array of integers
from array import *
a = array('i',[1,2,3,4,5,6,7,8])
sum = 0
for i in range(len(a)):
    sum= sum+a[i]
    avg = sum/len(a)
print("the sum of integers is ",avg)





#program to find index of an array element
from array import *
arr= array('i',[])
n = int(input("Enter the length of array :"))
for i in range(n):
    x=int(input("Enter the values :"))
    arr.append(x)
print(arr)
b = int(input("Enter the value to be searched :"))
print(arr.index(b))





#program to find a specific element in a array
from array import *
arr = array('i',[2,3,4,5,67,78,89,90])
value= int(input("Enter the value :"))
if value in arr:
    print("array contains value")
else:
    print("array does not contain value")





#function to remove specific element of array
from array import *
a=array('i',[1,2,3,4])
a.remove(2)
print(a)






#function to copy array to another array
from array import *
arr1=array('i',[1,2,3,4])
arr2=arr1
print(arr1)
print(arr2)






#insert an element in a specific position
from array import *
a=array('i',[1,3,5])
print(a)
a.insert(1,2)
print(a)
#min and max value
print(min(a))
print(max(a))
#reverse integers
a.reverse()
print(a)






# find duplicate elements in array
arr = [1,2,2,3,4,4,5,6,6,5]
print("Duplicte elements in given array")
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
            print(arr[j])





#pgm to find common value between 2 arrays
a=[1,2,3,4,5,6]
b=[2,4,8,9,7]
common_values=[i for i in a if i in b]
print(common_values)







#method to remove duplicates from an array
arr1 = [1,2,3,4,5,6,7,8,9,2,3,4,5]
arr2 = list(set(arr1))
print(arr2)







#method to find 2nd largest num in array
l=[]
n= int(input("enter length of list:"))
for i in range(1,n+1):
    m=int(input("Enter Elements :"))
    l.append(m)

print(l)
l.sort()
print("Second largest number is ",l[n-2])







#prgm to find number of even and odd numbers
def even_odd(arr,arr_size):
    even=0
    odd=0
    for i in range(arr_size):
        if (arr[i]%2)==0:
            even+=1
        else:
            odd+=1
    print("Number of even elements=",even)
    print("Number of odd elements=",odd)
arr=[2,3,4,5,6]
n=len(arr)
even_odd(arr,n)






#Prgm to find largest and smallest and smallest value
a=[]
n= int(input("Enter the length of list: "))
for i in range(n):
    x=int(input("Enter the elements : "))
    a.append(x)
print(a)
diff = max(a)-min(a)
print("difference between the largest and smallest value is", diff)







#program to find a specific element in a array
from array import *
arr = array('i',[2,3,4,5,12,78,89,23])
value= int(input("Enter the value :"))
if value in arr:
    print("array contains value")
else:
    print("array does not contain value")






#method to remove duplicates from an array
data = [1,2,3,4,5,6,7,8,9,2,3,4,5]
def remove_duplicate(list):
    c=[]

    for element in (list):
        if element not in c:
            c.append(element)
    return c
print(remove_duplicate(data))





#find missin num from 1 to 100
a=[0,1,2,3,5,6,7,8,9,10]
for i in range(101):
    if i not in a:
        print(i,"missing")