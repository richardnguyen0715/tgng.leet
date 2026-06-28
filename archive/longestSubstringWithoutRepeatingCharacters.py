class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            
            char_map[s[right]] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len
    
    

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Time: O(n^2)
        # Space: O(128)
        
        n = len(s)
        res = 0
        for i in range(n):
            seen = set()
            for j in range(i ,n):
                if s[j] in seen:
                    break
                else:
                    res = max(res, j - i + 1)
                    seen.add(s[j])
                    
        return res
    
    
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        ans = []
        set_char = set()
        start = 0  # Vị trí bắt đầu của substring hiện tại
        
        i = start
        while i < len(s):
            if s[i] not in set_char:
                set_char.add(s[i])
                i += 1
            else:

                ans.append(len(set_char))

                dup_char = s[i]

                # Tim vi tri bi trung dau tien trong chuoi hien tai -> tức là phần tử bị trùng có thể nằm ở bất cứ đâu trong chuỗi phân biệt hiện tại và ta phải lấy từ đó lấy lên chứ không phải lúc nào cũng trùng ở cuối cùng
                while start < i and s[start] != dup_char:
                    start += 1
                start += 1

                set_char = set()
                for j in range(start, i):
                    set_char.add(s[j])

                set_char.add(s[i])
                i += 1

        if set_char: # Substring cuoois cungf
            ans.append(len(set_char))

        return max(ans) if ans else 0


                
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # O(N) time
        # O(128) space
        
        n = len(s)
        res = 0

        seen = set()
        left = 0
        for right in range(n):
            c = s[right]

            while c in seen:
                
                if s[left] in seen:
                    seen.remove(s[left])
                left += 1

            res = max(res, right - left + 1)
            seen.add(c)
        
        return res
