import string
n = string.punctuation
a = input("Введите предложени: ")
def is_poliandrome(a):

    b = a[::-1]
    while True:
        if a[::1] ==b:

            return True
            break
        if a != b:
            return False
        continue

print(is_poliandrome(a))