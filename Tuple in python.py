# Tuple in python
# Immutable
# Surrounded by round brackets ex=> (1,1,5)

a=("naveen",25,"h",2.5,)
print(a)
print(type(a))
print(a[3]) 
b=list(a)
print(b)
print(type(b))
b.append("janani")
print(b)
a=tuple(b)
print(a)
print(a[0:2])
print(a[-1])
for i in a:    # we can use for loop also
    print(i)
if "naveen"in a: #checks condition using if
    print("naveen is found")
else:
    print("not found")
a=("naveen")
print(type(a))
a=("naveen",)
print(type(a))
del a #we can also delete elements in tuple
#print(a)
a=(5,4,3,1,2)
b=(3,2,1,7,8)
c=a+b
print(c)
print(c.count(2))
print("---------------------------------------------------")

#Nested tuples
c=(a,b)
print(c)
print(c[0])
print(c[1])
print(c[0][1])#slicing
n=("naveenjanu",)*5 # repitation of values
print(n)
print(max(a))
print(min(a))
print(len(a))


