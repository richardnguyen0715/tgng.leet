from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        # Chứa vị trí của các phần tử max trong từng window side - maxQueue
        candidates = deque()

        # add vào trước window đầu tiên (0 -> k - 1)
        for i in range(k):

            # Nếu mà nhỏ hơn thì không cần quan tâm đến phần tử đó nữa
            while candidates and nums[candidates[-1]] <= nums[i]:
                candidates.pop()
            
            # Thêm vị trí thứ i vào trong queue
            candidates.append(i)

        
        results = [0] * (n - k + 1) # 8 - 3 + 1 = 6

        for i in range( k - 1, n ):

            # Enqueue

            # Nếu mà nhỏ hơn thì không cần quan tâm đến phần tử đó nữa
            while candidates and nums[candidates[-1]] <= nums[i]:
                candidates.pop()
            
            # Thêm vị trí thứ i vào trong queue
            candidates.append(i)


            # Get max

            results [i - k + 1] = nums[candidates[0]]

            # Dequeue

            # current items
            if candidates and candidates[0] == i - k + 1: 
                candidates.popleft() # left vì lấy ra phần tử đầu tiên
            
        return results

        


        

        