from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        n = len(s)
        ans = 0
        left = 0
        cnt = Counter()
        
        
        for right in range(n):
            c = s[right]
            
            cnt[c] += 1
            
            while len(cnt) > k: # số lượng kí tự khác nhau xuất hiện vượt quá K lần
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    cnt.pop(s[left])
                left += 1
                
            ans = max(ans, right - left + 1)
            
        return ans
                
                
            
        
        