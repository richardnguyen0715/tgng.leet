
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        '''
        1. Valid Binary Tree Properties:
        - Each non-null node creates 2 children slots
        - Each node (null or non-null) fills 1 slot
        - Must end with exactly 0 available slots
        
        2. Slot Counting:
        - Start with 1 slot (for root)
        - Non-null node: -1 slot (fills current) + 2 slots (creates children) = +1 net
        - Null node: -1 slot (fills current) = -1 net
        - Valid if: end with 0 slots AND never negative during process

        3. Example Analysis:
        "9,3,4,#,#,1,#,#,2,#,6,#,#"
        
        slots = 1 (initial)
        9:  slots = 1 - 1 + 2 = 2  ✓
        3:  slots = 2 - 1 + 2 = 3  ✓
        4:  slots = 3 - 1 + 2 = 4  ✓
        #:  slots = 4 - 1 = 3      ✓
        #:  slots = 3 - 1 = 2      ✓
        1:  slots = 2 - 1 + 2 = 3  ✓
        #:  slots = 3 - 1 = 2      ✓
        #:  slots = 2 - 1 = 1      ✓
        2:  slots = 1 - 1 + 2 = 2  ✓
        #:  slots = 2 - 1 = 1      ✓
        6:  slots = 1 - 1 + 2 = 2  ✓
        #:  slots = 2 - 1 = 1      ✓
        #:  slots = 1 - 1 = 0      ✓ (end with 0)
        '''

        nodes = preorder.split(',')
        slots = 1
        
        for node in nodes:
            
            slots -= 1
            
            if slots < 0:
                return False
        
            if node != '#':
                slots += 2
        
        return slots == 0