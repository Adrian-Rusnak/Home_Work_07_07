import keyword
a = keyword.kwlist
result = True
b = input("Введите переменную: ")
for i in a :
    if i == b:
        result=False
if [s for s in b[0] if s in '''!"#$%&'()*+,-./:;<=>?@[\]^`{|}~''']:
    result = False
for i in b :
    if i.isupper():
        result=False
if b.istitle():
    result=False
if b.isdigit():
    result=False
if [s for s in b[0] if s in '1234567890']:
    result=False
print(result)




