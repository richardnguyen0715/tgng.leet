def romanToInt(s):
    dictionary = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    res = 0
    for i in range(0, len(s)-1):
        if s[i] == 'I' and dictionary[s[i+1]] > 1:
            res -= dictionary[s[i]]
        elif s[i] == 'X' and dictionary[s[i+1]] > 10:
            res -= dictionary[s[i]]
        elif s[i] == 'C' and dictionary[s[i+1]] > 100:
            res -= dictionary[s[i]]
        elif s[i] == 'M' and dictionary[s[i+1]] > 1000:
            res -= dictionary[s[i]]
        else:
            res += dictionary[s[i]]
    res += dictionary[s[-1]]
    return res