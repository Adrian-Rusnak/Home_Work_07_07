x = float(input("Введите число: "))
l = float(input("Введите второе число: "))
с = input("Выберите действие  +,-,/,* : ")
if с == "+":
    print(x+l)
elif с == "-":
    print(x-l)
elif с == "*":
    print(x*l)
elif с == "/":
    if l != 0:
        print(x/l)
else:
    print("на ноль не делится")
b = input("Хотите продолжить? (y/n): ")
while b == "y":
    x = float(input("Введите число: "))
    l = float(input("Введите второе число: "))
    с = input("Выберите действие  +,-,/,* : ")
    if с == "+":
        print(x + l)
    elif с == "-":
        print(x - l)
    elif с == "*":
        print(x * l)
    elif с == "/":
        if l != 0:
            print(x / l)
        else:
            print("на ноль не делится")
    b = input("Хотите продолжить? (y/n): ")
if b == "n":
    print("Робота окончена")
