# Handling multiple exceptions in python

try:
    a=10/5
    print(a)
    b=[10,20,30,40,50]
    print(b[5])
except ZeroDivisionError as e:
    print("denominator not to be zero")
except IndexError as e:
    print("invalid index")
    