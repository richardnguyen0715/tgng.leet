from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)

        freq = [[] for _ in range(n + 1)]

        freqCount = defaultdict(int)
        for num in nums:
            freqCount[num] += 1

        for key, val in freqCount.items():
            freq[val].append(key)
        
        res = []
        for i in range(n, -1, -1):
            if len(freq[i]) != 0 and k > 0:
                res.extend(freq[i])
                k -= len(freq[i])
        
        return res
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        ans = []
        for key, val in freq.items():
            ans.append((val, key))
        
        ans.sort(reverse=True)

        res = []
        for i in range(k):
            res.append(ans[i][1])
        
        return res