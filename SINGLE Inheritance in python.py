# SINGLE Inheritance in python

class nokia:              # base class
    mobile_no="12345"
    website="www.nokia.com"
    def contact_details(self):
        print("address  = 3/70,mathiyampatty")
class nokia_500(nokia):  # derived class
    def __init__(self):
        self.name= "nokia 500"
        self.model= "500" 
        self.year= "1996"
    def print_detail(self):
        print("name     = ",self.name)
        print("model    = ",self.model)
        print("year     = ",self.year)
        print("mobile no= ",self.mobile_no)
        print("website  = ",self.website)
object=nokia_500()
object.print_detail()
object.contact_details() 
        