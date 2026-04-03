
# Ước chung lớn nhất - Greatest Common Divisor
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Bội chung nhỏ nhất - BCNN
def lcm(a, b):
    return int(a / gcd(a, b)) * b

print(lcm(8,10))