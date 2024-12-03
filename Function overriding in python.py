# Function overriding in python

class employee:
    def working_hours(self):        # same definition
        self.working_hours=50
    def printhrs(self):
        print("total working hours is: ",self.working_hours)
        
class trainee(employee):
    def working_hours(self):        # But functionallity differs called overriding
        self.working_hours=60
    def resethrs(self):
        super().working_hours()     #super() by using this inbuilt function we can use base class function in derived class
        
        
object=employee()
object.working_hours()
object.printhrs()

object2=trainee()
object2.working_hours()
object2.printhrs()
object2.resethrs()
object2.printhrs()


        