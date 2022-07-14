l = [2,6,5,9,7,9,5,]
l1 = int(len(l) / 2)
l3 = len(l)
if l3 % 2 == 0:
    l, l2 = l[:l1], l[l1:]
    print([l, l2])

else:
    l, l2 = l[:l1 + 1], l[l1 + 1:]
    print([l, l2])
