def popular(t:str, l: list)-> dict:
    d ={}
    t =t.lower().split()
    for i in l:
        d[i]=t.count(i)
    return d
s = popular('''When I was One I had just begun When I was Two I was nearly new ''', ["i", "was","there","near"])
print(s)