
def gen(n):
    n = n**n
def some(gen):
    while True:
        yield gen+2
        gen =gen*2
v = some(gen(2))

print(gen(2))
print(some(gen(2)))


