import keyword
a = keyword.kwlist
c = [ '''*!"#$%&'()*+,-./:;<=>?@[\]^`{|}~''']
b = input("Введите переменную: ")
for i in a:
    if i == b :
        print(False)
for i in b:
    if i.isupper():
        print(False)
for i in c:
    if i[0]==b:
       print(False)
