# While else & For else
i=1
while i<=5:
    print(i)
    i+=1
else:
    print("Loop completed")
  
#if we use break in between program the else statement coudn't worked
i=1
while i<=5:
    if(i == 4):
        break;
    print(i)
    i+=1
else:
    print("Loop completed")
print("-------------------------------------")

#For loop
for i in range(20):
    print(i)
    i+=1
else:
    print("Loop completed")

