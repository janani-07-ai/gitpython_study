# Elif statement in python
"""
1-5 -> 0.5
5-10-> 1
10-30-> 5
>30-> Membership cancelled

"""
n=int(input("enter the no of days: "))
if (n == 0):
    print("no penality")

if (n >= 1 and n <= 5):
    print("the penality is :",n*0.5)
    
elif (n > 5 and n <= 10):
    print("the penality is :",n*1)
    
elif (n > 10  and n <= 30):
    print("the penality is :",n*5)
    
else:
    print("your membership is cancelled")
    
    
    
    