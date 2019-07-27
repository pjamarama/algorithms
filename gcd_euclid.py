a = int(input("Enter first nuber: "))
b = int(input("Enter second nuber: "))

def gcd_euclid(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd_euclid(a%b, b)
    elif a >= a:
        return gcd_euclid(b%a, a)

print(f"Greatest common divisor: {gcd_euclid(a, b)}")