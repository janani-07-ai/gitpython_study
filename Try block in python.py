# Try block in python
"""
a=10/0
print(a)
"""
try:
    a=10/0
except Exception as b:
    print(b)
else:
    print(a)
finally:
    print("thank you")
    