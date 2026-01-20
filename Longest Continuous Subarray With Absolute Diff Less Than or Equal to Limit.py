from typing import List



# Đúng một vài trường hợp nhưng sai nhiều trường hợp
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        import math

        n = len(nums)
        left = 0
        res_size = 0
        res = (0, (-1)*math.inf)

        while left < n:
            print("start : ", left)
            max_range = [(1, 0)] # (size, distance)
            right = left  + 1
            while right < n:
                print("left - right: ", left, right)
                distance = abs(nums[right] - nums[left])
                print("check distance: ", distance)
                while max_range and max_range[-1][1] <= distance:
                    print("distance - removed: ", max_range[-1])
                    max_range.pop()
                    print("after remove: ", max_range)

                new_max_distance = max(distance, max_range[-1][1]) if max_range else distance

                print("append: ", right - left + 1, new_max_distance)
                max_range.append((right - left + 1, new_max_distance))
                right += 1
                print("max range", max_range)
                print('------')

                if max_range:
                    temp_maxDistance = max_range[-1]

                    if res[0] <= temp_maxDistance[0] and res[1] <= temp_maxDistance[1] <= limit:
                        res = temp_maxDistance
                
                print("res: ", res)
            
            print("-----")
            left += 1

        return res[0]
    
    
# Solution chuẩn -> duy trì một minQueue và một maxQueue
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        # Time: O(N)
        # Space: O(N)
        
        # maxD luôn giảm dần

        # minD luôn tăng dần

        # maxD[0] và minD[0] luôn thuộc window

        # Khi left vượt qua một giá trị → phải pop nếu nó nằm ở đầu deque
        
        from collections import deque

        n = len(nums)
        left = 0
        maxQueue = deque()
        minQueue = deque()
        res = 0

        for right in range(n):
            
            while maxQueue and maxQueue[-1] < nums[right]: # Duy trì một max queue
                maxQueue.pop()
            
            maxQueue.append(nums[right]) # Ví dụ: [10], gặp 1 -> [10, 1], gặp 2 -> [10, 2]

            while minQueue and minQueue[-1] > nums[right]:
                minQueue.pop()

            minQueue.append(nums[right])

            while maxQueue[0] - minQueue[0] > limit:
                if nums[left] == maxQueue[0]: # Không lấy max đó nữa, do ta muốn duy chuyển left lên 1 đơn vị. Ví dụ [10, 1] mà distance là 9 -> loại bỏ 10, lấy 1
                    maxQueue.popleft()
                if nums[left] == minQueue[0]:
                    minQueue.popleft()
                
                left += 1

            res = max(res, right - left + 1)

        return res

