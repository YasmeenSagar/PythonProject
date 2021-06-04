# Collections
#ArrayList is similar to list in Python

l= ['1','2','3','python','5','6','7','8','9']
#add element
l.append("bye")
print(l)

#iterate over list
for i in l:
    print(i)
#add at specific index
l.insert(3,'4')
print(l)
# remove element at an index
l.pop(4)
print(l)
# update the element
l[4] = 'hii'
print(l)

# check element is present at perticular index

if l[2]=='3':
    print("True")
else:
    print("False")
# get element at perticular index
print(l[3])

# size of list
print(len(l))

if '3' in l:
    print("element present")
else:
    print("not present")

#remove all elements in array
l.clear()
print(l)








## Hashmap
d= {
    'Dev':'001',
    'ava':'002',
    'pri':'003',
    'den':'004',
    'abc':'005',
    'bad':'006',
    'roh':'007',
    'heer':'008',
    'mahi':'009',
    'richi':'010'
    }
#fetch the value of key
print(d['bad'])
#to check if given keys exist
key = input("enter key to be searched:")
if key in d.keys():
    print("Exists")
else:
    print("Not exists")

#to check if given value exist
value = input("enter value to be searched:")
if value in d.values():
    print("Exists")
else:
    print("Not exists")

# check if map is empty
has_items = bool(d)
print(has_items)            #dict has items

#size of map
print(len(d))

#print key values
print(d.keys())
print(d.values())

#remove a key value pair
d.pop('Dev')
print(d)







# Hash set
s={'1','2','3','4','5','6','7','8','9','10'}
s.pop()
print(s)
s.add(0)
print(s)
s.copy()
print(s)
s.remove('1')
print(s)
