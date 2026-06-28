from typing import List
import sys

# Tràn số -> set về 100000 :))))))))))))))))))))))))
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(100000)
        return [int(h) for h in str(int("".join([str(inter) for inter in num])) + k)]
    
    

    
