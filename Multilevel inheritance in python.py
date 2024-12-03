# Multilevel inheritance in python

"""
A
^
|
B
^
|
C

"""

class Grandfather:
    def grandpa_house(self):
        print("grandpa's house")
class father(Grandfather):
    def father_bike(self):
        print("father's bike")
class son(father):
    def son_book(self):
        print("his book")
object= son()
object.father_bike()
object.grandpa_house()
object.son_book()

