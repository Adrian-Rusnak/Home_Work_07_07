
def number(a):
    b = int(''.join(str (i) for i in a))+1

    c = [int(i) for i in str(b)]

    return c


print(number([9]))

