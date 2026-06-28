from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = 0
        self.next = None
    
def merged(List1: Optional[ListNode] = [], List2: Optional[ListNode] = []) -> Optional[ListNode]:

    if not List1 or not List2:
        return List1 or List2
    
    head, current = ListNode(), ListNode()
    head.next = current
    while List1 is not None and List2 is not None:
        if current.val > List1.val:
            current.next = List1
            List1 = List1.next
        if current.val > List2.val:
            current.next = List2
            List2 = List2.next
    
    if List1 is not None: 
        current.next = List1
    if List2 is not None:
        current.next = List2

    return head.next
        
    
def merged_ver2(List1: Optional[ListNode] = [], List2: Optional[ListNode] = []) -> Optional[ListNode]:

    if not List1 or not List2:
        return List1 or List2
    
    dummy = tmp = ListNode(0)
    while List1 and List2:
        if List1.val <= List2.val:
            tmp.next = List1
            List1 = List1.next
        else:
            tmp.next = List2
            List2 = List2.next
        # move to next node
        tmp = tmp.next
    
    tmp.next = List1 or List2

    return dummy.next
        
    
    