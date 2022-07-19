l = [1,0,2,3,0,5,0,4,0,6,7,8,0]
y = []
c = []
for x in l:
    if x == 0:
        y.append(x)
    else: c.append(x)
v = c+y
print(v)
