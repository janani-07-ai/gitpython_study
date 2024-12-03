# Nested if statement in python
'''

3 Marks as input
Total
Average
Result
If pass grade
    90-100   A
    80-89    B
    70-79    C
    Else     D
    
'''
m1=int(input("m1:"))
m2=int(input("m2:"))
m3=int(input("m3:"))
total=m1+m2+m3
print("total: ",total)
average=total / 3.0
print("average: ",average)
if (m1>=35 and m2>=35 and m3>=35):
    print("result: pass ")
    if average>=90 and average<=100:
        print("the student's grade is : A")
    elif average>=80 and average<=89:
        print("the student's grade is : B")
    elif average>=70 and average<=79:
        print("the student's grade is : C")
    else :
        print("the student's grade is : D")
else:
    print("result: fail")
    print("Grade : No grade")

