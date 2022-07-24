import keyword
a = keyword.kwlist
c = {*'''!"#$%&'()*+,-./:;<=>?@[\]^`{|}~'''}
b = input("Введите переменную: ")
for i in a:
    if i == b :
        print(False)
for i in b:
    if i[0].isupper():
        print(False)
    elif i[0] in b == c :
        print( false)