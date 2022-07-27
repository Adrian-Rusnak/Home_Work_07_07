import string
x = string.punctuation
h = input()
h = h.title()
h = h.split()
h = ''.join(h)
h = h.strip()
for i in h:
    if i in x:
        h = h.replace(i,"")
h[-1]= h[:140]

print(h)