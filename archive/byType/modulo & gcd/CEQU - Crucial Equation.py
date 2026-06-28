# Link: https://www.spoj.com/problems/CEQU/

def exGCD(a, b, x, y):
    if b == 0:
        x = 1
        y = 0
        return a

    q = int(a / b)
    r = int(a - b * q)
    x1 = 0
    y1 = 0
    d = exGCD(b, r, x1, y1)
    x = y1
    y = x1 - q * y1
    return d

def diophantineSolve(a, b, c):
    x = 0
    y = 0
    d = exGCD(a, b, x, y)
    if c % d != 0:
        return "No"

    x *= int(c/d)
    y *= int(c/d)
    
    if a < 0:
        x = -x
    
    if b < 0:
        y = -y
    
    return "Yes"


print(diophantineSolve(2, 4, 8))
print(diophantineSolve(3, 6, 7))
