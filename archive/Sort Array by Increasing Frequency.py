from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        freqMap = []

        for num in nums:
            isIn = False
            for i in range(len(freqMap)):
                if freqMap[i][0] == num:
                    freqMap[i][1] += 1
                    isIn = True
            if not isIn:
                freqMap.append([num, 1])
        
        freqMap.sort(key=lambda x: (x[1], -x[0]))
        
        res = []

        for freq in freqMap:
            res.extend([freq[0]] * freq[1])
        
        return res

            
        