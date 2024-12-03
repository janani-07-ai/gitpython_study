# Instance attributes in python

class user:
    course="python"       # class attributes
o=user()
print(user.course)        # class attributes
print(o.course)           # instance attributes 
o.course='java'
print(o.course)

o2= user()
print(o2.course)          # class attribute value only showned
o2.course= "html"
print(o2.course)  
