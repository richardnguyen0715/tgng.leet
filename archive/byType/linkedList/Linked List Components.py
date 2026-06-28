from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        linkedListVals = []
        cur = head
        while cur:
            linkedListVals.append(cur.val)
            cur = cur.next
        
        nums = set(nums)
        for idx, val in enumerate(linkedListVals):
            if val in nums:
                linkedListVals[idx] = -1
        
        ans = 0
        i = 0
        n = len(linkedListVals)
        # print(linkedListVals)
        while i < n:
            if linkedListVals[i] == -1:
                while i < n and linkedListVals[i] == -1:
                    i += 1
                ans += 1
                # print("got 1")
            i += 1
        
        print(ans)
        return ans



class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        linkedListVals = []
        cur = head
        nums = set(nums)
        
        while cur:
            if cur.val in nums:
                linkedListVals.append(-1)
            else:
                linkedListVals.append(cur.val)
            cur = cur.next
    
        ans = 0
        i = 0
        n = len(linkedListVals)
        # print(linkedListVals)
        while i < n:
            if linkedListVals[i] == -1:
                while i < n and linkedListVals[i] == -1:
                    i += 1
                ans += 1
                # print("got 1")
            i += 1
        
        print(ans)
        return ans