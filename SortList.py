from typing import Optional
from heapq import heapify, heappop
import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Time: O(NLogN)
        # Space: O(N)
        
        dummy = ListNode(0, head)
        runner = dummy.next
        heapList = []
        while runner:
            heapList.append(runner.val)
            runner = runner.next
        
        heapify(heapList)
        print(heapList)

        runner = dummy.next
        while runner:
            runner.val = heappop(heapList)
            runner = runner.next
        
        return dummy.next


# Time limit exceeded
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Time: O(N^2)
        # Space: O(1)
        
        dummy = ListNode(0, head)
        runner = dummy.next

        while runner and runner.next:
            fastRunner = runner.next
            while fastRunner:
                if runner.val > fastRunner.val:
                    temp = runner.val
                    runner.val = fastRunner.val
                    fastRunner.val = temp
                fastRunner = fastRunner.next
            runner = runner.next
            
        a = random.randint(0)
            
        return dummy.next
    
    
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Đếm số nodes
        n = 0
        current = head
        while current:
            n += 1
            current = current.next
        
        dummy = ListNode(0)
        dummy.next = head
        
        # Bottom-up merge sort
        size = 1
        while size < n:
            prev = dummy
            current = dummy.next
            
            while current:
                # Tách list1 có độ dài size
                list1 = current
                list1_tail = self.split(list1, size)
                
                # Tách list2 có độ dài size
                list2 = list1_tail.next if list1_tail else None
                list2_tail = self.split(list2, size) if list2 else None
                
                # Cập nhật current cho lần lặp tiếp theo
                current = list2_tail.next if list2_tail else None
                
                # Ngắt kết nối
                if list1_tail:
                    list1_tail.next = None
                if list2_tail:
                    list2_tail.next = None
                
                # Merge hai list đã sắp xếp
                merged_head = self.merge(list1, list2)
                prev.next = merged_head
                
                # Di chuyển prev đến cuối merged list
                while prev.next:
                    prev = prev.next
            
            size *= 2
        
        return dummy.next
    
    def split(self, head, size):
        """Tách list thành 2 phần: phần đầu có độ dài size, trả về tail của phần đầu"""
        if not head:
            return None
        
        current = head
        for i in range(size - 1):
            if current.next:
                current = current.next
            else:
                break
        
        return current
    
    def merge(self, list1, list2):
        """Merge 2 sorted linked lists"""
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Nối phần còn lại
        current.next = list1 or list2
        
        return dummy.next