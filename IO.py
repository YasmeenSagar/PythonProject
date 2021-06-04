# read file
f= open("files.txt",'r')
data = f.read()
print(data)
f.close()






#write a stream
with open("files.txt",'w')as a:
    b=a.write('bye')
print(b)






#pgm to read data from excel
import pandas as pd
data = pd.read_excel(r'C:\Users\NIRANJAN\Documents\book.xlsx')
print(data)






# pgm to write data to excel
import pandas as pd
df = pd.DataFrame({'States':['California','Montana',"Washington"],'Capitals':['Helena','Denver','Richmond']})
df.to_excel('./states.xlsx')
