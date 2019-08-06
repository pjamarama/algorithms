from sys import argv

def fib_multi(n):
    try:
        n = int(n)
    except ValueError:
        return "You should enter a number"

    assert n >= 0, "The number should be > 0"

    f0, f1 = 0, 1
    for i in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1

print(fib_multi(argv[1]))