# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        curr = head
        nums = []
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        left = 0
        right = len(nums) - 1
        maxSum = float("-inf")

        while left < right:
            maxSum = max(nums[left] + nums[right], maxSum)
            left += 1
            right -= 1
        
        return maxSum
