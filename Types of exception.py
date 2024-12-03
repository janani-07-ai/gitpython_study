# Types of exception in python

#print(dir(locals()['__builtins__']))
#print(len(dir(locals()['__builtins__'])))


# name error
try:
    print(a)
except NameError as e:
    print("put name on here")
#  Zero division error
try:
    a=10/0
except ZeroDivisionError as e:
    print("zero will not be divisible on denominator")
# value error
try:
    a=int("janu")
except ValueError as e:
    print("enter the numbers only")
# index error
try:
    a=[5,12,13,14,5]
    print(a[15])
except IndexError as e:
    print("denote corrrect index value")
# file not found error
try:
    a=open("test.txt")
    print(a.read())
except FileNotFoundError as e:
    print("file not found")
