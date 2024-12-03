# PRIME NUMBERS OR NOT

a=int(input("enter the number: "))
if a>1:
    for i in range(2,a):
        if a%i==0:
            print("not a prime number")
            break;
    else:
        print("prime number")
else:
    print("not a prime number")



