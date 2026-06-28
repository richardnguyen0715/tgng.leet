from collections import bisect
from typing import List


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


    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        # [[5,4],[6,4],[6,7],[2,3]]
        # [[2, 3], [5, 4], [6, 4], [6, 7]] -> Sau khi sort xong thì chỉ cần quan tâm đến chiều cao -> longest increasing subsequence
        # Note: các số ko phải unique -> khi mà bằng width thì ta sẽ ưu tiên lấy thằng nào có height cao hơn trước rồi thử thằng nhỏ hơn -> do đó nếu như bằng width thì ta sẽ sort giảm dần height

        # Sort tăng dần, nếu x[0] bằng nhau thì sort giảm dần theo x[1]
        envelopes.sort(key=lambda x: [x[0], -x[1]]) 
        
        # Sau sort thì chỉ cần quan tâm đến height thôi, vì width đã tăng dần rồi
        array = [h for _, h in envelopes]

        return self.longestIncreasingSubsequence(array)
        