# Instance method
class student:
    name= "janani"
    age =  25
    
    def printall(self):
        print("name is: ",student.name)
        print("age is: ",student.age)
object=student()
object.printall()
# another method
class student:
    name= "janani"
    age =  25
    
    def printall(self,gender):
        print("name is: ",student.name)
        print("age is: ",student.age)
        print("gender is: ",gender)
            
object=student()
object.printall('male')
