class TrieNode:

    def __init__(self):
        self.finished = False
        self.child = {}
        self.sum = 0


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.valueMap = {}
        

    def insert(self, key: str, val: int) -> None:
        
        offset = 0
        if key in self.valueMap:
            oldValue = self.valueMap[key]
            offset = val - oldValue
        else:
            offset = val
            
        self.valueMap[key] = val
        
        node = self.root
        for char in key:
            child = node.child.get(char, None)
            if not child:
                child = TrieNode()
                node.child[char] = child
            node = child
            child.sum += offset
        node.finished = True
        
    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            child = node.child.get(char, None)
            if not child:
                return 0
            node = child
        
        return node.sum

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)