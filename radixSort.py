import math


def mainSort(nums):
    
    # Time: O(N * Log10(maxValue))
    # Space: O(N * Log10(m))
    
    maxValue = max(nums)
    maxLength = len(str(maxValue)) # hoặc int(math.Log10(maxValue) + 1)
    
    for length in range(maxLength):
        nums = radixSort(nums, length)
        print("i - nums: ", length, nums)
    
    return nums


# Build up from counting sort
def radixSort(nums, k):
    n  = len(nums)
    c = [0] * 10 # max digit = 9 -> maxVal + 1 = 10
    
    for i in range(n):
        digit = getDigit(nums[i], k)
        c[digit] += 1
        
    for i in range(1, 10):
        c[i] += c[i - 1]
        
    result = [0] * n
    for i in range(n - 1, -1, -1):
        digit = getDigit(nums[i], k)
        result[c[digit] - 1] = nums[i]
        c[digit] -= 1
    
    return result

def getDigit(num, k):
    return int((num / math.pow(10, k)) % 10)


print(mainSort([1, 222, 4, 345, 678, 329, 456, 293]))