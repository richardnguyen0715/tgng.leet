class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        n = len(nums1)
        
        minOdd = None
        
        for x in nums1:
            if x % 2 != 0:  
                if minOdd is None or minOdd > x :
                    minOdd = x
        
        for target in (0, 1):
            fullCount = 0
            for i in range(n):
                if nums1[i] % 2 == target:
                    fullCount += 1
                elif minOdd is not None and minOdd < nums1[i]:
                    fullCount += 1
            if fullCount == n:
                return True
        
        return False
                    