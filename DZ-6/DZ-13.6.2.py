b = input("Введите число: ")
c = str.split(b)
c = ''.join(c)
if len(c)== 1:
    c = 1
elif len(c)== 2:
    c = str(int(c[0])*int(c[1]))
elif len(c)==3:
    c = str(int(c[0]) * int(c[1])*int(c[2]))
while int(c) >9:
    if len(c) == 1:
        c = 1
    elif len(c) == 2:
        c = str(int(c[0]) * int(c[1]))
    elif len(c) == 3:
        c = str(int(c[0]) * int(c[1]) * int(c[2]))


print(c)

