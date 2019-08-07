a = int(input("Enter first nuber: "))
b = int(input("Enter second nuber: "))

def gcd_euclid(a, b):
    assert a > 0 and b > 0
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= b:
        return gcd_euclid(a % b, b)
    else:
        return gcd_euclid(b % a, a)

def gcd3(a, b): # recursion, no condition statements
    assert a > 0 and b > 0
    if a == 0 or b == 0:
        return max(a, b)
    return gcd3(b % a, a)

# Stepik example no recursion
def gcd2(a, b):
    while a and b:
        if a >= b:  
            a %= b # a is swapped with remainder
        else:
            b %= a
    return max(a, b) # number !=0 is returned 

print(f"Greatest common divisor: {gcd_euclid(a, b)}")

