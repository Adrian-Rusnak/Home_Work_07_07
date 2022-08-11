def chislo(a):
    b = []
    for i in a:
        if i in b:
            continue
        else:
            b.append(i)

    return b
print(chislo([1,2,1,1,1]))