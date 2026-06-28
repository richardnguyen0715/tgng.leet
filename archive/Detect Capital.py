class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
    
class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        upper = 0
        lower = 0
        flag = False
        n = len(word)
        
        for i, char in enumerate(word):
            if 'A' <= char <= 'Z':
                upper += 1
                if i == 0:
                    flag = True
            
            else:
                lower += 1
        
        print(upper, lower, flag)
        
        if n == upper:
            return True
        
        if n == lower:
            return True
        
        if upper == 1 and flag:
            return True
        
        return False
        