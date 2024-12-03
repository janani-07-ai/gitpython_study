# Class methods in python
class student:
    name= "janani"
    age =  25
    
    def printall():
        print("name is: ",student.name)
        print("age is: ",student.age)
student.printall()
print((student.__dict__['printall']))

        