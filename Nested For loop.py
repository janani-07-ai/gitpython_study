# Nested For loop
'''
*
**
***
****
*****
ASCII VALUE
A-Z-----> 65-90
a-z-----> 97-122

'''

for i in range(5):
    for j in range(i):
        print("*",end="")#we put end in here to print all in one line 
    print("\n")#this is used to go for next line
print("---------------------------------")
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("\n")
print("---------------------------------")
for i in range(65,71,1):
    for j in range(65,71,1):
        print(chr(j),end="")
    print("\n")

    
     