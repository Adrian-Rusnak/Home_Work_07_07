v=0

def name(a , c):
    v =a.find(c)
    if v == a.find(c):
        v = a.find(c, v +1)
        if v == -1:
            return None
        else:
            return v

print(name("find the river", "e"))



