
def gen(n):
    n = n**2
    return n
def some(start,a, gen):
    while start <= a  :
        yield start
        start =gen(start)
v = some(2, 256, gen)




print(next(v))
print (0)
print(next(v))
print (0)
print(next(v))
print (0)
print(next(v))