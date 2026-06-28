from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # Time: O(2^N * ( N + NLogN ) + N)
        # Space: O(N + N) = O(N)

        n = len(nums)
        res = set()
        
        for i in range(0, 2 ** n): # O(2^N)
            path = []
            for j in range(0 , n): # O(N)
                if (i >> j) & 1 == 1: # Tức là dãy bit i, tại vị trí j có giá trị là 1, tương ứng nums[j] có tồn tại trong path
                    path.append(nums[j])
            
            if path:
                path.sort() # O(NLogN)
            res.add(tuple(path))
        
        return [list(ans) for ans in res]  # O(N)
    
    

# [[4,4],[4,4,1,4],[4,4,4,4],[4,1,4],[4,4,1],[4],[1,4],[4,4,4],[1],[4,4,4,1,4],[],[4,1],[4,4,4,1]]

# [] [1][1,4]

# [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
