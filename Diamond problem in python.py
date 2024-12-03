# Diamond problem in python

"""
            A
            ^
    B               C
    ^                ^
            D
            
"""

class A:
    def display(self):
        print("I am the display of A")
        
class B(A):
    #def display(self):
        #print("I am the display of B")                 # overriding
        pass
        
class C(A):
    #def display(self):
       # print("I am the display of C")                 # overriding
       pass
        
class D(B,C):
    #def display(self):
        #print("I am the display of D")                 # overriding
        pass
        
object=D()
object.display()   
  
        
            