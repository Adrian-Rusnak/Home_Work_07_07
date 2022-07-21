x = float(input("Введите число: "))
y = float(input("Введите второе число: "))
с = input("Выберите действие  +,-,/,* : ")
a = ("N")
m = ("Y")
if с == "+":
    print(x+y)
    b = str(input("Хотите продолжить? (Y/N): "))
elif с == "-":
    print(x-y)
    b = str(input("Хотите продолжить? (Y/N): "))
elif с == "*":
    print(x*y)
    b = str(input("Хотите продолжить? (Y/N): "))
elif с == "/":
    if y != 0:
        print(x/y)
        b = str(input("Хотите продолжить? (Y/N): "))
    else:
        print("на ноль не делится")
while b == "Y":
    x = float(input("Введите число: "))
    y = float(input("Введите второе число: "))
    с = input("Выберите действие  +,-,/,* : ")
    if с == "+":
        print(x + y)
        b = str(input("Хотите продолжить? (Y/N): "))
    elif с == "-":
        print(x - y)
        b = str(input("Хотите продолжить? (Y/N): "))
    elif с == "*":
        print(x * y)
        b = str(input("Хотите продолжить? (Y/N): "))
    elif с == "/":
        if y != 0:
            print(x / y)
            b = str(input("Хотите продолжить? (Y/N): "))
        else:
            print("на ноль не делится")
else:
    print("Робота окончена")
