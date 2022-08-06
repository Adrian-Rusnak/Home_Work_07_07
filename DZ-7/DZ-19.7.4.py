import random
l=[]
k = []

for i in range (50) :
    if i %3==0:
        l.append(i)
for x in range(50):
    if x %5==0:
        k.append(x)
m = set(l)
n = set(k)
p = m.intersection(n)
print(l)
print(k)
print(p)