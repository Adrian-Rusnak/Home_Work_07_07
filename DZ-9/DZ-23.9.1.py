def massiv(*args):
    if len(args)== 0:
        return 0
    else:
        m = max(args)-min(args)
        return m
print(massiv(1,2,3,5,9))