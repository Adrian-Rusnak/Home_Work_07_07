def popular(text:str, lst: list)-> dict:
    dct ={}
    text = text.lower().split()
    for word in lst:
        dct[word]=text.count(word)
    return dct
res = popular('''When I was One I had just begun When I was Two I was nearly new ''', ["i", "was","there","near"])
print(res)