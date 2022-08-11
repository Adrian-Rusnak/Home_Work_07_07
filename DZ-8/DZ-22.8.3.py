def chislo(a):
    b = []
    for i in a:
        if i in b:
            continue
        else:
            b.append(i)

    return b
print(chislo([20,20,30,30,40]))