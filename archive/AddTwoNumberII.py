from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# Beat: 41% Time, 7% Space
# Time: O(max(M,N,K)), M : len(l1), N : len(l2), K : len(Sum)
# Space: o(M + N)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1, num_2 = [], []

        while l1:
            num_1.append(str(l1.val))
            l1 = l1.next
        
        while l2:
            num_2.append(str(l2.val))
            l2 = l2.next
        
        print(num_1)
        print(num_2)

        numSum = str(int("".join(num_1)) + int("".join(num_2)))
        
        dummy = ListNode(0, None)
        temp = dummy
        for char in numSum:
            newNode = ListNode(int(char))
            temp.next = newNode
            temp = temp.next
            
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Beat: 100% Time, 8% Space
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Directly Stimulation
        num_1, num_2 = [], []

        while l1:
            num_1.append(l1.val)
            l1 = l1.next
        
        while l2:
            num_2.append(l2.val)
            l2 = l2.next
        
        memo = 0
        temp = None
        while num_1 and num_2:
            last_1 = num_1.pop()
            last_2 = num_2.pop()
            sumVal = last_1 + last_2 + memo
            memo = sumVal // 10
            sumVal %= 10
            newNode = ListNode(sumVal, temp)
            temp = newNode

        while num_1:
            last_1 = num_1.pop()
            sumVal = last_1 + memo
            memo = sumVal // 10
            sumVal %= 10
            newNode = ListNode(sumVal, temp)
            temp = newNode
        
        while num_2:
            last_1 = num_2.pop()
            sumVal = last_1 + memo
            memo = sumVal // 10
            sumVal %= 10
            newNode = ListNode(sumVal, temp)
            temp = newNode

        if memo > 0:
            newNode = ListNode(memo, temp)
            temp = newNode

        return temp

            