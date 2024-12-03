# -*- coding: utf-8 -*-

s_username="EMC"
s_password= "123"

uname=input("Enter the username:")
password=input("Enter the password: ")
def validate():
    if (s_username==uname and s_password==password):
        return True
    else:
        return False
print(validate())

