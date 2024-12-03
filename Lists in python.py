
# Lists in python
'''
Sequence type
Mutable type

'''

a=[1,2,3,4,5]#equential type
print(a[4])
a[1]=50#mutable type
print(a)
print(a[0:3])#slicing
print(a[-1])
print("-----------------------------------------------------------------")

# By using list we can use multiple data types in one sequence
a=[5,False,3.5,'j',[1,2,3]]#we can also use nested list into it
print(a)
print(a[3])
print(a[2],"the type is: ",type(a[2]))
print(a[4],"the type is: ",type(a[4]))
print(a[4][2])
print("-----------------------------------------------------------------")

#Some inbuilt functions of list

a=[20,30,40,50,60]
print(a)
a.clear()
print(a)
a=[20,30,40,50,60]
b=a.copy()
print(b)
print(a.count(20))
print(a.index(20))
print(len(a))
print(max(a))
print(min(a))
a.pop(0)     # remove element using index
print(a)
a=[20,30,40,30,50]
a.remove(30) #remove value of first occcurance
print(a)
print("-----------------------------------------------------------------")

# append and extend functions

name=["naveen"]
print(name)
name.append("kumar")
name.append("married")
name.append("janani")
print(name)
plan=["and they want to built a big career"]
name.extend(plan)
print(name)
name.insert(0,"love")
print(name)
print("-----------------------------------------------------------------")

#List constructor
# it makes the senteces or numbers as single element 
#that what we should give it to be

a=list(range(5))
print(a)
a=list("frustruating")
print(a)
print("-----------------------------------------------------------------")

#sorting methods

a=[10,45,20,5,15]
print(a)
a.sort() #ascending
print(a)
a.sort(reverse=True) #Descending
print(a)
a=["i LOVE","bedsheets","pillows","of mine"]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.sort(key=len)
print(a)



