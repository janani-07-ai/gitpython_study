# Static method in python

class triple:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def printdetail(self):
        print("name is ",self.name, "age is", self.age)
    @staticmethod
    def welcome(): #we don't ut self instance on here we use static means it's common to all classes and objects
        print("welcome to our triple")
object=triple("janu","25")
object.printdetail()
object.welcome()

        