x = float(input("Введите число: "))
y = float(input("Введите второе число: "))
с = input("Выберите действие(+,-,/,*: ")
if с == "+":
    print(x+y)
elif с == "-":
    print(x-y)
elif с == "*":
    print(x*y)
elif с == "/":
    if y != 0:
        print(x/y)
    else:
        print("на ноль не делится")


