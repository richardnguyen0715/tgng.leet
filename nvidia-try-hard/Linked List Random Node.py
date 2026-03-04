from typing import Optional
import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.root = head
        self.array = []
        runNode = head
        while runNode:
            self.array.append(runNode.val)
            runNode = runNode.next

    def getRandom(self) -> int:
        return self.array[random.randint(0, len(self.array) - 1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()