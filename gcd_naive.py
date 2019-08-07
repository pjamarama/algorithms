a = int(input("Enter first nuber: "))
b = int(input("Enter second nuber: "))

def gcd_naive(a, b):
    assert a > 0 and b > 0
    for d in reversed(range(2, max(a, b))):
        if a%d == b%d ==0:
        # if (a%d == 0) and (b%d == 0):
            return d
    return "No common devisor exept 1"

print(gcd_naive(a, b))


        
