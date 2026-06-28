from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        
        for left, right in intervals[1:]:
            
            last = res[-1]
            
            if last[1] >= left:
                last[1] = max(last[1], right)
            else:
                res.append([left, right])
                
        return res