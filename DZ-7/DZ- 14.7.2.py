def propozition(a):
    a = [i for i in a]
    a[0] = a[0].upper()
    if a[-1] =='.':
        return ''.join(a)
    else:
        a.append(".")
        return''.join(a)
d = propozition('greetings friends')
print(d)
