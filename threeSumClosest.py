from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]

        for idx in range(n - 2):
            left = idx + 1
            right = n - 1

            while left < right:
                cur_sum = nums[idx] + nums[left] + nums[right]

                if abs(target - cur_sum) < abs(target - ans):
                    ans = cur_sum

                if cur_sum == target:
                    return target
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1

        return ans
