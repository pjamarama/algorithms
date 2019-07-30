"""
looking for last digit of a Fibonacci number
"""

a = int(input("Enter the nuber: "))

def fib_last_digit(n):
    arr = [0] * (n+1)
    for i in range(n+1):
        if i == 0:
            arr[i] = 0
        elif i == 1:
            arr[i] = 1
        else:
            arr[i] = (arr[i-1] + arr[i-2]) % 10
    return arr[i]


print(fib_last_digit(a))