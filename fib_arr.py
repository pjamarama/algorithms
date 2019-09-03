a = int(input("Введите порядковый номер числа Фибоначчи: "))

def fib_arr(n):
    arr = [0] * (n+1)
    for i in range(n+1):
        if i == 0:
            arr[i] = 0
        elif i == 1:
            arr[i] = 1
        else:
            arr[i] = arr[i-1] + arr[i-2]
    return arr[i]

print(f"{a}-е число Фибоначчи: {fib_arr(a)}")