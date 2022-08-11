import string
n = string.punctuation
a = input("Введите предложени: ").lower()
def is_polindrome(a):
    a = a.replace(" ", "")
    for i in n:

            a = a.replace(i,'')
    b = a[::-1]
    return b ==a
print(is_polindrome(a))