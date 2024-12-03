# property decorators Getter & Setter in python
'''
class student:
    def __init__(self,total):
        self.total=total
    def avg(self):
        return self.total/5.0
object=student(479)
print(object.total)
print(object.avg())
object.total=450
print(object.total)
print(object.avg())
'''

# we made an encapsulation of these datas
class student:
    def __init__(self,total):
        self._total=total
    def avg(self):
        return self._total/5.0
    @property                  # this is getter functions
    def total(self):
        return self._total
    @total.setter              # this is setter  # by using this function we have to use data validations
    def total(self,t):
        if t<=0 or t>=500:
            print("Invalid data")
        else:
            self._total=t
object=student(490)
print(object.total)
print(object.avg())
object.total=530
print(object.total)
print(object.avg())
