def threeSum(nums):
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate a

            l, r = i + 1, n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    # skip duplicate b
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # skip duplicate c
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return res

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4, 2]
    print(threeSum(nums))
