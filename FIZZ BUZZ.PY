# FIZZ BUZZ
"""
write a program to print numbers from 1 to 100
For multiplies of 3,print "FIZZ"
For multiplies of 5,print "BUZZ"
For multiplies of both 3 and 5 ,print FIZZ BUZZ

"""
a= 1
while a<=100:
    if a%3==0 and a%5==0:
        print("FIZZ BUZZ")
    elif a%3==0:
        print("FIZZ")
    elif a%5==0:
        print("BUZZ")
    else:
        print(a)
    a+=1