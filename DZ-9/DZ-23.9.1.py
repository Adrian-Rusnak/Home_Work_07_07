def massiv(a):
    if a == []:
        return 0
    b= a[0]
    c = a[0]
    for i in a:
        if i > b:
            b=i
    for i in a:
        if i <c:
            c=i
    return b-c
print(massiv([5,-5]))



m =(5,-5)
if m==():
    print(0)
else:
    c = max(m)-min(m)
    print(c)