from collections import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [] # lưu giá trị của các số
        indices = [] # lưu index mà phần tử đó trỏ vào
        trace = [-1] * len(nums)

        for idx, num in enumerate(nums):
            if not sub or sub[-1] < num:
                if sub:
                    trace[idx] = indices[-1]
                sub.append(num)
                indices.append(idx)
            else:
                # Mục tiêu là khi tìm thấy thằng nhỏ hơn thằng cuối cùng của sub thì ta sẽ thay thế nó bằng thằng đầu tiên mà lớn hơn hơn hoặc bằng nó trong sub (bisect_left). Ví dụ 2 6 8, num = 3 thì ta sẽ thay thế thành 2 3 8. Note: sub không phải là longest increasing, nhưng len của sub chính là độ dài của longest increasing (vì ta không pop ra mà thay thế trực tiếp)
                idx_f = bisect.bisect_left(sub, num)
                

                if idx_f > 0:
                    trace[idx] = indices[idx_f - 1]
                
                sub[idx_f] = num
                indices[idx_f] = idx

            
        path = []
        t = indices[-1]
        while t >= 0:
            path.append(nums[t])
            t = trace[t]
        
        print(path[::-1])

        return len(sub)
    

class Solution:

    def longestIncreasingSubsequence(self, nums):
        sub = []
        for num in nums:
            if not sub or sub[-1] < num:
                sub.append(num)
            else:
                idx = bisect.bisect_left(sub, num)

                sub[idx] = num
        
        return len(sub)