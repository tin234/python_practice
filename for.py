import random

a = range(0, 10, 2)
b = enumerate(a)

for x, y in b:
    c = (x,)
    print(c)


def string_gen():
    while not None:
        yield random.random()


i=5
for x in string_gen():
    if i > 0:
        i -= 1 
        print(x)
    else: 
        break