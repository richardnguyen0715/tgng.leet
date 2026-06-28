from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Reverse đoạn [left, right] bằng cách reverse in-place
        Time: O(n), Space: O(1)
        """
        if not head or left == right:
            return head
        
        # Dummy node để xử lý trường hợp reverse từ head
        dummy = ListNode(0)
        dummy.next = head
        
        # Bước 1: Tìm node trước vị trí left
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        # Bước 2: Reverse đoạn [left, right]
        # prev -> node1 -> node2 -> node3 -> ... -> after
        #         (left)                      (right)
        
        current = prev.next  # Node đầu tiên cần reverse (left)
        
        for _ in range(right - left):
            # Lấy node tiếp theo
            next_node = current.next
            
            # Ngắt kết nối
            current.next = next_node.next
            
            # Chèn next_node vào đầu đoạn đã reverse
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next