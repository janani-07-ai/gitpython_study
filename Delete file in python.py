# Delete file in python

import os
# if os.path.exists("hello.txt")
if os.path.exists("hifi"):
    #os.remove("hello.txt")
    os.rmdir("hifi")           # to delete a folder
else:
    print("file not found")
    
    