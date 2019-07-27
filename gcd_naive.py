a = int(input("Enter first nuber: "))
b = int(input("Enter second nuber: "))

def gcd_naive(a, b):
    for d in range(2, max(a, b)):
        if (a%d == 0) and (b%d == 0):
            return d
    return "No common devisor exept 1"

print(gcd_naive(a, b))


        
