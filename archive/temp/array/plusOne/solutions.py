def plusOne(digits):
    res = 0
    for i in range(0, len(digits)):
        res += 10**(len(digits)-i-1) * digits[i]
    res += 1
    return [int(x) for x in str(res)]