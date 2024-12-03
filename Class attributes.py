# Class attributes in python
# First we have to use attributes by two different types of operations
# inbuilt function
# dot notation

class handbag:
    name= "lavie"
    price= 550
    colour="sandal"
print(getattr(handbag,"name"))
print(getattr(handbag,"price"))
print(getattr(handbag,"colour"))

# another method
print(handbag.name)
print(handbag.price)
print(handbag.colour)

# this function is to set attributes in two ways

setattr(handbag,'name','clutch')
print(handbag.name)

#another method
handbag.name='golden'
print(handbag.name)

handbag.size ='medium'
print(handbag.size)
print(handbag.__dict__)

# how to del attributes

delattr(handbag,'size')
print(handbag.__dict__)
# anothe method
del(handbag.colour)
print(handbag.__dict__)


      