from typing import List
import random



# Time limit exceeded
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Time: N + N/2 + N/4 + N/6 + ... << 2*N -> O(N)
        
        return self.kthLargest(nums, 0, len(nums) - 1, k)
        
    def swap(self, nums, i , j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
        
    def kthLargest(self, nums, left, right, k):
        if left == right:
            return nums[left]
        
        print("left - right: ", left, right)
        print("nums", nums)
        
        pivot = left + random.randint(0, right - left)
        print(pivot)
        self.swap(nums, pivot, right)
        count = left
        for i in range(left, right):
            if nums[i] >= nums[right]:
                print("swap i count :", i , count)
                self.swap(nums, count, i)
                count += 1
            
        self.swap(nums, count, right)
        
        if count == k - 1:
            return nums[count]
        elif k - 1 < count:
            print("Go left")
            return self.kthLargest(nums, left, count - 1, k)
        else:
            print("Go right")
            return self.kthLargest(nums, count + 1, right, k)
        

a = [3, 2, 1, 5, 6, 4]
sol = Solution()
print(sol.findKthLargest(a, 3))
    
