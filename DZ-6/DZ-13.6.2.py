x = int(input('Ввод числа: '))
y = (x//86400)
c = (x%86400)
u = (c//3600)
i = (c%3600)
b =(i//60)
v = (i%60)
if y ==0:
    u,b,v = 00,00,00
    print(y, "дней", u,":",b,":",v)
elif  y < 2:
    print(y, "день", u,":",b,":",v)
elif  y <= 4:
    print(y, "дня", u,":",b,":",v)
elif y <=20:
    print(y, "дней", u,":",b,":",v)
elif y%10 ==1:
    print(y, "день", u,":",b,":",v)
elif y%10 <=4:
    print(y, "дня", u, ":", b, ":", v)
elif y%10 <=9:
    print(y, "дней", u, ":", b, ":", v)
