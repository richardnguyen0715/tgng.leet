class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        
        n = len(nums)

        ansSet = set()

        for i in range(n - 2):

            # fix the first ele is nums[i]
            left = i + 1
            right = n - 1

            # print(i, left, right)

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ansSet.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        
        # print(ansSet)

        return [list(ans) for ans in ansSet]



class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        
        n = len(nums)

        res = []

        for i in range(n - 2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            # fix the first ele is nums[i]
            left = i + 1
            right = n - 1

            # print(i, left, right)
            while left < right:

                currSum = nums[i] + nums[left] + nums[right]

                if currSum == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif currSum > 0:
                    right -= 1
                else:
                    left += 1
            
        return res