class TrieNode:
    
    def __init__(self):
        self.is_end = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            child = node.children.get(char, None)
            if not child:
                child = TrieNode()
                node.children[char] = child
            node = child
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            child = node.children.get(char, None)
            if not child:
                return False
            node = child
        return node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            child = node.children.get(char, None)
            if not child:
                return False
            node = child
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)