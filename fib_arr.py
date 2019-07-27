def fib_arr(n):
    # arr = [0] * n
    # # arr[0] = 0
    # # arr[1] = 1
    # print(f"arr = {arr}")
    # for i in range(n):
    #     print(i)
    #     if i == 0:
    #         arr[i] = 0
    #     elif i == 1:
    #         arr[i] = 1
    #     else:
    #         arr[i] = arr[i-1] + arr[i-2]
    # return arr[i]

    arr = [0] * (n+1)
    for i in range(n+1):
        if i == 0:
            arr[i] = 0
        elif i == 1:
            arr[i] = 1
        else:
            arr[i] = arr[i-1] + arr[i-2]
    return arr[i]

print(f"100-е число Фибоначчи: {fib_arr(100)}")