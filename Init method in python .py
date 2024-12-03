# Init method in python (called Constructor)

class user:
    def __init__(self,name):
        print("when object is created init function automatically called we can assign any values and messages whenever creating object easily.....")
        self.name=name
    def printall(self):
        print("name is: ",self.name)
object=user("janu")
object.printall()
object1=user("naveenkumar")
object1.printall()