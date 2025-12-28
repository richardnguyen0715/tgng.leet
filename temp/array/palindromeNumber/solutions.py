def isPalindrome1(x):
    if x < 0:
        return False
    compare = 0
    original = x
    while (int(x) > 0):
        compare = compare*10 + (int(x%10))
        x /= 10
    # print(compare)
    if compare != original:
        return False
    return True

def isPalindrome2(x):
    str_x = str(x)
    len_x = len(str_x)
    for i in range(0, len_x//2):
        if str_x[i] == str_x[len_x-i-1]:
            continue
        else:
            return False
    return True

def isPalindrome(x):
    str_x = str(x)
    return str_x == str_x[::-1]