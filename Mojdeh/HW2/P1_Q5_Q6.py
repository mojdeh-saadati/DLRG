# In python when we assign a new varible to another varible, both varibles will refer to same object in memory and have the same refrence number. 
# Therefore, change in value of one will change the value in the othe one. However, if we use deepcopy we will create two object and the content of first 
# object will be coppied to the second one. In this way the two objects points out to different locations in memory. 

X = [int(item) for item in  input().split(" ")]
Y = [int(item) for item in  input().split(" ")]
Res = []
for i, (m, n) in enumerate(zip(X,Y)):
    if m > n:
         Res.append((i, m))   
print(Res)
Res = []
for i, (m, n) in enumerate(zip(X,Y)):
    if m == n:
         Res.append((i))   
print(Res)
