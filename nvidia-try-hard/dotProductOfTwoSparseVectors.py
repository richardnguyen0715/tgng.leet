from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.vec = { i : v for i, v in enumerate(nums) if v}

    def dotProduct(self, vec: 'SparseVector') -> int:
        
        smaller, larger = (self.vec, vec.vec) if len(self.vec) < len(vec.vec) else (vec.vec, self.vec)
        
        res = 0
        for idx, val in smaller.items():
            res += val * larger[idx]
        
        return res