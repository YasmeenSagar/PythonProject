#STRINGS

#different ways of creating a string
my_string = 'Hello'
print(my_string)
my_string = "Hello"
print(my_string)
my_string = '''123'''
print(my_string)






#Concatinating 2 string
str1 = "Hello"
str2 = "World"
str = str1 + str2
print(f"Concatination of str1 and str2 is {str}")







#Finding the length of the string
str = "Python"
print(len(str))

# without in built
c=0
for i in "Python":
    c+=1
print(c)







#Extracting substring
s = "Hello World"
print(s[0:5])
print(s[6:])







#searching in string using find()
s = "Hello Good Afternoon"
print(s.find("Good"))
print(s.index("f"))







#Trim a string using strip()
data = "   hello   "
print(data.strip())






#splitting string using split()
txt = " welcome, to the new home , iam yasmeen"
# txt ="welcome"
print(txt.split(", "))






#replacing with replace()
a = "Java is good"
print(a.replace("Java","Python"))






#comparing strings
s1 = "Eddy"
s2= "David"
s3= "Eddy"
print(s1==s2)
print(s2==s3)
print(s3==s1)






#convert int to str
i = 123
c=str(i)
print(c)
print(type(c))







#converting to upper and lowercase
s1= "Iam THANKFULL to the Reader"
print(s1.lower())
print(s1.upper())







#equals ignore case
s1= "HELLO"
s2 = "hello"
if s1.lower() == s2.lower():
    print("Both are same")
else:
    print("Both are different")







#Startswith() ad endswith
a = "This is a story related to my life"
print(a.startswith("This"))
print(a.startswith("this"))
print(a.endswith("you"))
print(a.endswith("life"))






#compareTo in python
s1 = "yasm"
s2 = "yaseen"
if len(s1)== len(s2):
    print(str(0))
elif len(s1) > len(s2):
    print(str(1))
else:
    print(str(-1))






# string with regex
import re
x = 'this , is ,a , sample , line'
re.match("sample",x)
if re.search("sample",x):
    print("found match")
else:
    print("No match")









