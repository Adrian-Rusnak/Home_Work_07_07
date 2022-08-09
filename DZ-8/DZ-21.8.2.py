import string
n = string.punctuation
a = input("Введите предложени: ").lower()
def is_polindrome(a):
    for i in a:
        if i in n:
            a = a.replace(i,'')
    b = a[::-1]
    while True:
        if a[::1] ==b:
            return True
            break
        if a != b:
            return False
        continue
print(is_polindrome(a))