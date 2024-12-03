# Readline and readlines in python

try:
    file=open("test.txt","r")
    #print(file.readline())
    #print(file.readline(11))  # we can access read comment as by character by character
    #print(file.readlines())   # all the lines in file shows in list format
    
    for line in file:          
        print(line)            # we can also access lines in looping concepts 
        
except FileNotFoundError:
    print("choose the correct file name")
else:
    file.close()
