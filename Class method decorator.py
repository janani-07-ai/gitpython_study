# Class method decorator

class students:
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        students.count+=1
    def printdetail(self):
        print("name is: ",self.name , "age is:",self.age)
    @classmethod
    def total(cls): # if it's a class method so instance of self we uses cls on here
        return cls.count

o=students("naveen","28")
o.printdetail()
print("total admision of students:",o.total())

o1=students("mariyappan","50")
o1.printdetail()

print("total admision of students:",students.total())


