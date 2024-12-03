# Write or Overwrite in python

# write and overwrite
 
try:
    file= open("test.txt","w")
    file.write("it's so haappy by god's grace")
    file.close()
    
    file= open("test.txt","r")
    print(file.readline())

except FileNotFoundError:
    print("make sure your file name was correct or not")

else:
    file.close()