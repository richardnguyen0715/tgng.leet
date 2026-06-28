class Solution:
    def reverseByType(self, s: str) -> str:
        
        letters = []
        lettersIdx = []
        special = []
        specialIdx = []

        for idx, char in enumerate(s):

            if ord('a') <= ord(char) <= ord('z'):
                letters.append(char)
                lettersIdx.append(idx)
            else:
                special.append(char)
                specialIdx.append(idx)
        
        res = [''] * len(s)
        letters = letters[::-1]
        special = special[::-1]
        
        m, n = 0, 0
        for i in lettersIdx:
            res[i] = letters[m]
            m += 1
        for j in specialIdx:
            res[j] = special[n]
            n += 1
        
        return "".join(res)
    
    

class Solution:
    def reverseByType(self, s: str) -> str:
        
        letterStack = []
        specialStack = []

        for char in s:
            if 'a' <= char <= 'z':
                letterStack.append(char)
            else:
                specialStack.append(char)
            
        res = []
        for char in s:
            if 'a' <= char <= 'z':
                res.append(letterStack.pop())
            else:
                res.append(specialStack.pop())
        
        return "".join(res)