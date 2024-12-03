# Property method in python

class user:
    def __init__(self,total):
        self._total=total
    def avg(self):
        return self._total/5.0
    def getter(self):
        return self._total
    def setter(self,t):
        if t<=0 or t>=500:
            print("invalid data")
        else:
            self._total =t
    total=property(getter,setter)
        
o=user(450)
print(o.total)
print(o.avg())
o.total= 350
print(o.total)
print(o.avg())


        