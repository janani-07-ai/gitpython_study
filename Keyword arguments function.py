# 1
# Keyword arguments function in python

def data(name,age):
    print(name,"age is",age)
data(age=25,name="janu")

# 2
# Arbitrary Keyword arguments function in python

def message(** data):
    print(data)
    
message(name="naveen kumar",age=28,gender="male",marital_status="married")

# 3
# Default argument parameter function in python

def clear(name,place="salem"):
    print(name, "from",place )
    
clear("janu","namakkal")
clear("naveen")

# 4
# Passing a list as an argument in function

def total(marks):
    return sum(marks)
print(total([80,70,90,60]))

# 5
# Recursive function
# 1*2*3*4*5 = 120

def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
print(factorial(5))

""" working of this function
factorial(5)
5*factorial(5-1)
5*4*factorial(4-1)
5*4*3*factorial(3-1)
5*4*3*2*factorial(2-1)
x==1 means it returns
5*4*3*2*1 = 120
"""

# 6
# Lambda function in python

c= lambda a:a+20
print(c(20))

c= lambda a,b:a/b
print(c(15,3))