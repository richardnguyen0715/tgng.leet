from typing import List



class RSTNode:
    def __init__(self):
        self.child = {} # Dùng dict hơi tốn bộ nhớ -> có thể chuyển qua dùng list [None, None]
        self.value = 0
        
class Solution:

    def findMaximumXOR(self, nums: List[int]) -> int:
        root = RSTNode()
        
        for value in nums:
            self.insert(root, value)
            
        res = 0
        for value in nums:
            # res = max(res, value ^ self.getXor(root, value)) # Cách này bị OOM
            res = max(res, self.getXor(root, value))
            
        return res
    

    def insert(self, root: RSTNode, value: int):
        node = root
        for i in range(31, -1, -1):
            bit = (value >> i) & 1
            child = node.child.get(bit, None)
            if not child:
                child = RSTNode()
                node.child[bit] = child
            node = child
        node.value = value


    # Cách này bị OOM
    # def getXor(root: RSTNode, value: int):
    #     node = root
    #     for i in range(31, -1, -1):
    #         bit = (value >> i) & 1
    #         child = node.child.get(1 - bit, None)
    #         if not child:
    #             child = node.child.get(bit)
    #         node = child
        
    #     return node.value
    
    # Cách này cũng bị out of mem
    # def getXor(self, root: RSTNode, value: int):
    #     node = root
    #     xor_val = 0
    #     for i in range(31, -1, -1):
    #         bit = (value >> i) & 1
    #         toggled = 1 - bit
    #         if toggled in node.child:
    #             xor_val |= (1 << i)
    #             node = node.child[toggled]
    #         else:
    #             node = node.child[bit]
    #     return xor_val
            
        
        
        
from typing import List

# Giảm 70-80 MEM khi ko cần lưu value và ko cần lưu child bằng map, thay vào đó là list với 2 giá trị bit 0 hoặc 1
class RSTNode:
    __slots__ = ('child',)

    def __init__(self):
        self.child = [None, None]

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = RSTNode()

        for v in nums:
            self.insert(root, v)

        ans = 0
        for v in nums:
            ans = max(ans, self.query(root, v))

        return ans

    def insert(self, root: RSTNode, val: int):
        node = root
        for i in range(31, -1, -1):
            bit = (val >> i) & 1
            if node.child[bit] is None:
                node.child[bit] = RSTNode()
            node = node.child[bit]

    def query(self, root: RSTNode, val: int) -> int:
        node = root
        res = 0
        for i in range(31, -1, -1):
            bit = (val >> i) & 1
            opposite = 1 - bit
            if node.child[opposite] is not None:
                res |= (1 << i)
                node = node.child[opposite]
            else:
                node = node.child[bit]
        return res


# Không dùng Trie mà sử dụng greedy
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        mask = 0
        res = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            prefixes = {num & mask for num in nums}
            candidate = res | (1 << i)
            if any((candidate ^ p) in prefixes for p in prefixes):
                res = candidate
            
        return res
