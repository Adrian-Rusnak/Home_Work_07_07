y = int(input("Ввод числа: "))
x = (y%10)*10000+(y//10%10)*1000+(y//100%10)*100+ (y//1000%10)*10+(y//10000)
print(x)
