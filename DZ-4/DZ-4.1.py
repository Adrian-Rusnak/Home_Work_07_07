import random
l=[]
for i in range (10):
    l.append(random.randint(3,10))
print(l)

x,y,b = l[0],l[2],l[-2]
n = [[x]+[y]+[b]]
print(n)
