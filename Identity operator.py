# Identity operator
# output comes with boolean operations
# checking objects
"""
is 
is not

"""
a=[5,3,1]
b={5,3,1}
c=a
print(id(a))
print(id(c))#checks memory location
print(id(b))
print(a is c)#it checks objects only not element, #is operator
print(a is b)
print(a is not c)#is not operator
print(a is not b)


