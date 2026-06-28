from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        preNum = curr.val
        curr = curr.next
        idx = 1
        ansPos = []
        ans = [-1, -1]
        while curr:
            if curr.next:
                flag = False
                if preNum > curr.val and curr.val < curr.next.val:
                    ansPos.append(idx)
                    flag = True

                if preNum < curr.val and curr.val > curr.next.val:
                    ansPos.append(idx)
                    flag = True

                if flag and len(ansPos) > 1:
                    minDistance = idx - ansPos[-2]
                    maxDistance = idx - ansPos[0]
                    ans[0] = min(minDistance, ans[0]) if ans[0] != -1 else minDistance
                    ans[1] = max(maxDistance, ans[1]) if ans[1] != -1 else maxDistance
            
            preNum = curr.val
            curr = curr.next
            idx += 1
        return ans
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
            prev, curr = head, head.next
            pos = 1
            first_cp = last_cp = None
            min_dist = float('inf')

            while curr.next:
                if curr.val > prev.val and curr.val > curr.next.val or \
                curr.val < prev.val and curr.val < curr.next.val:
                    if last_cp is not None:
                        min_dist = min(min_dist, pos - last_cp)
                    if first_cp is None:
                        first_cp = pos
                    last_cp = pos
                prev = curr
                curr = curr.next
                pos += 1

            if first_cp == last_cp or first_cp is None:
                return [-1, -1]

            return [min_dist, last_cp - first_cp]