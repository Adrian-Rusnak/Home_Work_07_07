import keyword
a = keyword.kwlist
c = [ '''*!"#$%&'()*+,-./:;<=>?@[\]^`{|}~''']
b = input("Введите переменную: ")
for i in a:
    if i == b:
        print(False)
if b.isupper():
    print(False)
if b.istitle():
    print(False)
for i in c:
    if i[0]==b:
       print(False)
if b.isdigit():
    print(False)
if [s for s in b[0] if s in '1234567890']:
    print(False)
else:
    print(True)
