from typing import List


# Beat: 5.05% time, 8.32% space
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        # Time: O(NLogN + N + LogN + N) = O(NLogN)
        # Space: O(N)
        
        nums.sort()
        n = len(nums)
        ans = 0
        prefixSum = [0] * (n + 1)

        # Tính prefix sum để tìm tổng băng O(1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        
        def getSum(left, right):
            # [1, 2, 4] có prefixsum là [0, 1, 3, 7] -> [0:2] = 7 - 0 = 7
            return prefixSum[right + 1] - prefixSum[left]

        def findSmallestIndex(i):
            left = 0
            right = i
            ans = i

            while left <= right:
                mid = (left + right) // 2
                # Mục tiêu là thử fill toàn bộ các phần tử nhỏ hơn nó tới mid bằng i (vị trí hiện tại)
                # Khi fill hết hết thì chính là nums[i] * (i - mid + 1)
                # Trừ cho tổng hiện tại sẽ ra chênh lệch hiện tại để fill -> chúng chính là số k cần để fill
                cntK = nums[i] * (i - mid + 1) - getSum(mid, i)
                
                # Tìm cntK nhỏ nhất (xa i nhất)
                if cntK <= k:
                    ans = mid # Index xa i nhất mà có khả năng fill lên bằng nums[i]
                    right = mid - 1
                else:
                    left = mid + 1
            
            return ans


        for i in range(n):
            j = findSmallestIndex(i)
            ans = max(ans, i - j + 1) # i sẽ lớn hơn j vì i đi trước j (hàm trên tìm trái nó nhất mà xa nó nhất mà thoã điều kiện)
        
        return ans