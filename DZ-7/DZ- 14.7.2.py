def propozition(A, B):
    A = A.title()
    B = ''.join(B)
    if B[-1] ==".":
        return A, B
    else:
        B = B.split()
        B.append(".")
    B = ''.join(B)
    return A,B
d = propozition('Greetings ', 'friends.')
print(d)
