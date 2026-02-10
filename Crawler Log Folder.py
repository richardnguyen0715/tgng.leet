from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        n = len(logs)
        steps = 0
        for i in range(n):
            if logs[i] != "../" and logs[i] != "./":
                steps += 1
            
            if logs[i] == "../":
                steps -= 1
            
            if steps <= 0:
                steps = 0
            
        return steps
            
        