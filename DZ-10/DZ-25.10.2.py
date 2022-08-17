x = list(input('Ввод'))
def gen(x):
    return x**x[0]
def some(start=gen):
    while some <= gen:
        yield start
        start =gen(start)
v = some()

print(list(some()))


