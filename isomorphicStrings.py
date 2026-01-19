class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # Time: O(N)
        # Space: O(2N) = O(N)
        
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):

            char_s, char_t = s[i], t[i]

            if char_s in s_to_t: # O(1)
                if char_t != s_to_t[char_s]:
                    return False
            else:
                s_to_t[char_s] = char_t

            
            if char_t in t_to_s: # O(1)
                if char_s != t_to_s[char_t]:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # Time: O(N)
        # Space: O(N)
        
        # set(zip(s,t)) -> các cặp ánh xạ có trong s và t: {('g', 'd'), ('e', 'a')}
        
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))



class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # O(N) - Time - Early Stopping
        # O(N) - Space
        
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}
        
        for i in range(len(s)):
            char_s, char_t = s[i], t[i]
            
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                if char_t in t_to_s:
                    return False
                s_to_t[char_s] = char_t
                t_to_s[char_t] = char_s
        
        return True
        