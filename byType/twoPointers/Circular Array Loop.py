class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)
        
        def getNext(i):
            return (i + nums[i]) % n
        
        for i in range(n):
            if nums[i] == 0:
                continue
                
            slow = fast = i
            
            while nums[fast] * nums[i] > 0 and nums[getNext(fast)] * nums[i] > 0:
                slow = getNext(slow)
                fast = getNext(getNext(fast))
                
                if slow == fast:
                    if slow == getNext(slow):
                        break
                    return True
            
            slow = i
            val = nums[i]
            while nums[slow] * val > 0:
                next_slow = getNext(slow)
                nums[slow] = 0
                slow = next_slow
        
        return False