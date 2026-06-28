from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root or not root.left:
            return root
        
        root.left.next = root.right

        if root.next:
            root.right.next = root.next.left
        
        self.connect(root.left)
        self.connect(root.right)

        return root
    
    
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        levelStart = root
        while levelStart.left:
            current = levelStart
            while current:
                current.left.next = current.right

                if current.next:
                    current.right.next = current.next.left
                
                current = current.next
            levelStart = levelStart.left
    
        return root