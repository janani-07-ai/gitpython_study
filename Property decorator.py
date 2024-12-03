# Property decorator in python

class user():
    def __init__(self,name,age):
        self.name= name
        self.age= age
        # 1 st method # self.msg= self.name + "  your age is :"+str(self.age)
# 2nd method
    def msg(self):
        return self.name + "  your age is :"+str(self.age)
object=user("naveenkumar","28")
print(object.name)
print(object.age)
print(object.msg())# msg is now a function so we use() symbol
object.age= 35
print(object.msg())

# 3rd method
# use decorative property for converting function as property
class user():
    def __init__(self,name,age):
        self.name= name
        self.age= age
    @property
    def msg(self):
        return self.name + "  your age is :"+str(self.age)
object=user("naveenkumar","28")
print(object.name)
print(object.age)
print(object.msg)# msg is now a not a function so we don't use() symbol
object.age= 35
print(object.msg)


