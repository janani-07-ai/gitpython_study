# Append file in python

try:

    file= open("janu.txt","a+")
    file.write("Thanks for asking")
    file.close()
    
    file= open("janu.txt","r")
    print(file.read())

except FileNotFoundError:
    print("make sure your file name was correct or not")

else:
    file.close()
    
