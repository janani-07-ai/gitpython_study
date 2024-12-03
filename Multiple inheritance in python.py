#   Multiple inheritance in python


class father:                          # base class
    def fishing(self):
        print("fishing with father")
    def chess(self):
        print("playing chess with father")
class mother:                         # base class
    def cooking(self):
        print("cooking with mother")
    def chess(self):
        print("playing chess with mother")
class son(father,mother):                           # derived class
    def ride(self):
        print("riding with me")
object=son()
object.fishing()
object.cooking()
object.ride()
object.chess()
