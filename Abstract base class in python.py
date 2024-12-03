# Abstract base class in python

# first we have to import abstract package
# in this method we don't put defnitions on functions of base class
# we define their functions in their derived classes only
 
from abc import ABC,abstractmethod

class bank(ABC):             # ABC = inheritance of the base class
    @abstractmethod
    def loans(self):
        pass
    @abstractmethod
    def credits(self):
        pass
    @abstractmethod
    def interest(self):
        pass
class SBI(bank):
    def loans(self):
        print(" we provide personal loans")
    def credits(self):
        print(" credit cards are provided")
    def interest(self):
        print(" interst are very low 1.5%")
    def goldloan(self):
        print(" 1 kg per interest 0.75 %")
object=SBI()
object.loans()
object.credits()
object.interest()
object.goldloan()
