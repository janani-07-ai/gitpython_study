# Dictionary functions
user={
      "name":"janani",
      "age":"25",
      "marital status":"True",
      }
print(user)
print(user["name"])
print(user.get("age"))
print(user.keys())
print(user.values())
print(user.items())
print("-------------------------------------------------")
for x in user:
    print(x," ",user[x])
for x in user.keys():
    print(x)
for x in user.values():
    print(x)
for x,y in user.items():
    print(x,y)
if "age" in user:
    print("yes present")
user.update({"gender":"female"})
print(user)
user.pop("age")
print(user)
user["marital status"]="False"
print(user)
user.clear()
print(user)

users={
       "user1":
           {
           "name":"naveen",
           "age":"28",
           "gender":"male" ,          
             },
       "user2":
           {
           "name":"janani",
           "age":"25",
           "marital status":"True",
           
           }
       }
print(users)


