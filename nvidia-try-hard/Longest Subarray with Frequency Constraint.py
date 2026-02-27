from collections import defaultdict

def solution(nums, k):
    
    if not nums:
        return 0
    
    freq = {}
    n = len(nums)
    left = 0
    currAns = 0
    ans = 0
    
    for right in range(n):
        
        num = nums[right]
        
        if num not in freq:
            freq[num] = 1
            currAns += 1
        else:
            freqNum = freq[num]
            if freqNum == k:
                while left <= right and nums[left] != num:
                    left += 1
                    # Remove
                    if freq[nums[left]]:
                        freq[nums[left]] -= 1
                        if freq[nums[left]] == 0:
                            del freq[nums[left]]
                    currAns -= 1
                
                left += 1
                currAns -= 1
            else:
                freq[num] += 1
                currAns += 1
                
        ans = max(ans ,currAns)
                    
    return ans
            
                
print(solution([1, 2, 1, 2, 3, 1], 2))