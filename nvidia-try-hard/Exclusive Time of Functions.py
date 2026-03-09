from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        res = [0] * n
        prev = 0
        stack = []
        
        for log in logs:
            fid, typ, ti = log.split(":")
            fid = int(fid)
            ti = int(ti)
            
            if typ == 'start':
                
                if stack:
                    res[stack[-1]] += ti - prev
                
                stack.append(fid)
                prev = ti
            
            else:
                
                res[stack.pop()] += ti - prev + 1
                prev = ti + 1
        
        return res