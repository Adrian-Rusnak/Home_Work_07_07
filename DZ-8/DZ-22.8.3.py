def chislo(a):
    c=[]
    b = []
    for i in a:
        if a .count(i)>1:
            c.append(i)
        else:
            b.append(i)
            return b[0]


print(chislo([5,5,5,0.5]))