class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        if len(palindrome) <= 1:
            return ""
        
        n = len(palindrome)
        ord_a = ord('a')

        res = ""

        def isPalindrome(s):
            return s[::-1] == s

        for i in range(n):
            char_i = palindrome[i]
            ord_i = ord(char_i)

            if ord_i != ord_a:
                candidates = palindrome[:i] + 'a' + palindrome[i+1:]
            else:
                candidates = palindrome[:i] + 'b' + palindrome[i+1:]
            
            print("res: ", res)
            print("candidate: ", candidates)
            
            if candidates < res and candidates != palindrome and not isPalindrome(candidates) or res == "":
                res = candidates
        
        return res
    
    
# Ý tưởng số 2:
# Tìm thằng khác a đầu tiên đổi thành a rồi return, nếu toàn là a thì đổi phần tử cuối thành 'b'

def breakPalindrome(palindrome):
    
    n = len(palindrome)
    
    if n <= 1:
        return ""

    chars = list(palindrome)
    
    for i in range(n // 2): # Vì là palindrome nên ta chỉ cần xem xét n // 2
        if chars[i] != 'a':
            chars[i] = 'a'
            return "".join(chars)
    
    # Nếu toàn là a thì đổi phần tử cuối thành 'b'
    chars[-1] = 'b'
    return "".join(chars)
        