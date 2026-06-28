class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, len(nums))

    def mergeSort(self, nums, n):
        if n <= 1:
            return nums
        
        mid = n // 2
        left = nums[:mid]  # from 0 to mid - 1
        right = nums[mid:]  # from mid to n - 1

        left_half = self.mergeSort(left, len(left))
        right_half = self.mergeSort(right, len(right))

        return self.merge(nums, left_half, right_half, len(left), len(right))
    
    def merge(self, nums, left, right, n, m):
        i, j, count = 0, 0 ,0
        while (i < n) and (j < m):
            if left[i] < right[j]:
                nums[count] = left[i]
                count += 1
                i += 1
            else:
                nums[count] = right[j]
                count += 1
                j += 1

        while (i < n):  # left is still remain the values
            nums[count] = left[i]
            count += 1
            i += 1  


        while (j < m):  # right is still remain the values
            nums[count] = right[j]
            count += 1
            j += 1  

        return nums