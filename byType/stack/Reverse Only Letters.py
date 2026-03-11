class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letterStack = []

        for char in s:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                letterStack.append(char)
            
        res = []
        for char in s:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                res.append(letterStack.pop())
            else:
                res.append(char)
        
        return "".join(res)