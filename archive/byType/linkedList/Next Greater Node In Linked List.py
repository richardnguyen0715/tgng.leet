from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        runNode = head
        nums = []
        while runNode:
            nums.append(runNode.val)
            runNode = runNode.next
        
        n = len(nums)
        ans = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):

            curNum = nums[i]
            
            while stack and nums[stack[-1]] <= curNum:
                stack.pop()
            
            if stack:
                ans[i] = nums[stack[-1]]
            stack.append(i)
        
        print(ans)
        return ans
