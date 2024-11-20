a = [x for x in range(1, 11, 1)]

for x in a:
    print(x)
    if x % 2 == 0:
        print(x)

for index, x in enumerate(a):
    print(f"{index}: {x}")

args = {"sep": "__", "end":"the end"}
print(*a, **args)
print()

def square_numbers(numbers):
    for num in numbers:
        yield num ** 2

for square in square_numbers(a):
    print(square)

print(*square_numbers(a))
