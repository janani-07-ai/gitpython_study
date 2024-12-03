# Read a Text file in python

file=open("test.txt","r")
print(file.read())

# incase file name i wrong so that exception we made try block function

try:
    file=open("teest.txt","r")
    print(file.read())
except FileNotFoundError:
    print("choose the correct file name")
else:
    file.close()
    