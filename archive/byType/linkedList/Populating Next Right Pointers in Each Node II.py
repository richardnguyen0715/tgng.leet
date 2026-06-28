from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = deque()
        queue.append((0, root))

        while queue:
            level, node = queue.popleft()

            # print("current_level: ", level, node.val)

            if node.left:
                queue.append((level + 1, node.left))
            
            if node.right:
                queue.append((level + 1, node.right))

            curr = node
            while queue:
                level2, node2 = queue.popleft()

                if level2 > level:

                    queue.appendleft((level2, node2))
                    break
                else:
                    curr.next = node2
                    
                curr = node2
                if curr.left:
                    queue.append((level + 1, curr.left))
                
                if curr.right:
                    queue.append((level + 1, curr.right))
        
        return root

            