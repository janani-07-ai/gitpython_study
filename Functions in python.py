# Functions in python
# always use word "def" in before making function


def hi():
    print("hi naveenjanu")
# we can proceed how much time we call a function 
hi()
hi()
hi()
print("-----------------------------------------------------")
# Type -1
# No return type Without arguments function

def add():
    a=int(input("Enter the value of a :"))
    b=int(input("Enter the value of b :"))
    c=a+b
    print("the total is:",c)
    
add()
print("-----------------------------------------------------")

# Type -2
# No return type With arguments function

def sub(a,b):
    c=a-b
    print("difference : ",c)
sub(20,10)
print("-----------------------------------------------------")

# Type -3
# return type Without arguments function

def mul():
    a=int(input("Enter the value of a :"))
    b=int(input("Enter the value of b :"))
    c=a*b
    return c
x=mul() 
print("mult: ",x)
print("-----------------------------------------------------")

# Type -4
# return type With arguments function  

def div(a,b):
    c=a/b
    return c
x=div(20,5)
print("div: ",x)
print("-----------------------------------------------------")


# Arbitrary arguments function in python (*)
# We can access vast amount of values into the function as arbitrary ,it can takes it as list

def class_10(*students): # star before fuction is denoted as arbitrary
    print(students)
    for user in students:
        print(user)
class_10("naveen","janu","radha","kishore")
print("-----------------------------------------------------")





