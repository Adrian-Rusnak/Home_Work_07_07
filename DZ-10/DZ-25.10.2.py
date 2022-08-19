
def gen(n):
    n = n**2
    return n
def some(start, gen, a):
    while start <= a  :
        yield start
        start =gen(start)
v = some(2, gen, 256)




print(next(v))
print (0)
print(next(v))
print (0)
print(next(v))
print (0)
print(next(v))