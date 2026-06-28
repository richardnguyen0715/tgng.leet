def solution(s):
    
    if len(s) == 0:
        return 0


    set_character = set()
    ans = 0
    right = 0
    start = 0
    n = len(s)
    
    while right < n:
        
        char = s[right]
        
        if char not in set_character:
            set_character.add(char)
        else:
            
            ans = max(ans, len(set_character))
            
            while start < right and s[start] != char:
                start += 1
            start += 1 # Skip char
            
            set_character = set()
            # Copy to new set
            for i in range(start, right + 1):
                set_character.add(s[i])
        
        right += 1
        
    
    return ans


print(solution("abcdcaaadddbcd"))
            
            
                
    