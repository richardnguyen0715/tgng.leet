
# O(N) - O(N) - Beat: 33%
class Solution01:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n = len(nums)

        max_val = [0] * n
        min_val = [0] * n

        # setup
        max_val[0] = nums[0]
        min_val[n-1] = nums[n-1]

        # Get max
        for idx in range(1, n):
            max_val[idx] = max(max_val[idx - 1], nums[idx])
        
        # Get min
        for idx in range(n - 2, -1, -1):
            min_val[idx] = min(min_val[idx + 1], nums[idx])

        
        for idx in range(n):
            if max_val[idx] - min_val[idx] <= k:
                return idx
        
        return -1


# O(N) - O(N) - Beat: 64% with early stopping
class Solution02:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n = len(nums)

        max_val = [0] * n
        min_val = [0] * n

        # Init
        max_val[0] = nums[0]
        min_val[n-1] = nums[n-1]

        # Get min first - because we need to find smallest index
        for idx in range(n - 2, -1, -1):
            min_val[idx] = min(min_val[idx + 1], nums[idx])
        
        if max_val[0] - min_val[0] <= k:
            return 0

        # Get max
        for idx in range(1, n):
            
            # Solution 3: remove max_val; just keep 1 variable to save the current max at index idx (Beat 100%)
            max_val[idx] = max(max_val[idx - 1], nums[idx])
            if max_val[idx] - min_val[idx] <= k:
                return idx

        return -1