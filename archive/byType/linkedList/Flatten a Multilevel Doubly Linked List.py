from collections import deque

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        current = head
        
        while current:
            if current.child:
                # Save the next node
                next_node = current.next
                
                # Connect current to child
                current.next = current.child
                current.child.prev = current
                
                # Find the tail of the child branch
                child_tail = current.child
                while child_tail.next:
                    child_tail = child_tail.next
                
                # Connect child tail to the saved next node
                if next_node:
                    child_tail.next = next_node
                    next_node.prev = child_tail
                
                # Clear the child pointer
                current.child = None
            
            current = current.next
        
        return head