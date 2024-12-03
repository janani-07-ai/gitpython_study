# Set & it's function in python
# Unordered and unindexed datatype
a={"janu","naveen","thangam","thangamama"}
print(a)
print(type(a))
#assigning values 
for i in a:
    print(i)
# adding new element
a.add("love")
print(a)
#remove and discard function
a.remove("thangam")
print(a)
a.discard("thangamama")
print(a)
print("-----------------------------------------")
#update another set of data
b={5,2,3}
a.update(b)
print(a)
a.clear()
print(a)
print("-----------------------------------------")
#Not accept the duplicate values
a={1,2,1,2,3,4,5}
print(a)
print("-----------------------------------------")

#union and update function
a={1,4,5,6,7}
b={3,8,9,5,6}
c=a.union(b)
print(c)
b.update(a)
print(b)
print("-----------------------------------------")
#intersection function
a={1,4,5,6,7}
b={3,8,9,5,6}
c=a.intersection(b)
print(c)
b.intersection_update(a)
print(b)
print("-----------------------------------------")
#symetric difference
a={1,4,5,6,7}
b={3,8,9,5,6}
c=a.symmetric_difference(b)
print(c)
b.symmetric_difference_update(a)
print(b)
print("-----------------------------------------")
a={1,4,5,6,7}
b={5,6,7}
c=a.isdisjoint(b)
print(c)
c=b.issubset(a)
print(c)
c=b.issuperset(a)
print(c)
    

