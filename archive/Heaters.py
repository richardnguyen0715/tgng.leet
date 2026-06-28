from typing import List
from collections import bisect


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        # Time: O(NLogN + MLogN) M = |houses|, N = |heaters|
        # Space: O(sorting(N))
        # Ý tưởng cơ bản là tìm 2 chặn left right với các heater của từng ngôi nhà xong lấy max của các ngôi nhà.
        # Right là tìm phần tử đầu tiên lớn hơn target -> -1 là ra nhỏ hơn hoặc bằng target. Nếu không tìm thấy thì return về len(nums)
        # Left là tìm phần tử đầu tiên lớn hơn hoặc bằng target -> nếu không tìm thấy thì về len(nums)

        import math

        heaters.sort()
        ans = -math.inf
        for i in houses:
            neededRadius = math.inf
            left_max = bisect.bisect_right(heaters, i) - 1

            if left_max >= 0:
                neededRadius = min(neededRadius, i - heaters[left_max])

            right_min = bisect.bisect_left(heaters, i)

            if right_min < len(heaters):
                neededRadius = min(neededRadius, heaters[right_min] - i)

            
            ans = max(ans, neededRadius)
        
        return ans
            