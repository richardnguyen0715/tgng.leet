from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next
        
        base = cnt // k
        extra = cnt % k

        cur = head
        ans = []
        for i in range(k):
            preHead = cur

            size = base + (1 if i < extra else 0)

            for j in range(size - 1):
                if cur:
                    cur = cur.next
                
            if cur:
                nextNode = cur.next
                cur.next = None
                cur = nextNode
            
            ans.append(preHead)
        
        return ans