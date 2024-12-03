# Operator overloading in python
"""
a=5
b=10
print(a+b) # here + is an  operator that overloads result

a ="naveen"
b ="janu"
print(a+b)

"""
class factor:
    def __init__(self,a):
        self.a=a
    def __add__(object1,object2):       # use this magic functions to operate objects
        return object1.a + object2.a
    def __sub__(object1,object2):
        return object1.a - object2.a
    
object1=factor(10)
object2=factor(20)


print("addition of objects:", object1 + object2)
print("subtraction of objects:", object1 - object2)
    