class TrieNode:
    def __init__(self):

        self.finished = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    # Space: O(M*N) M là số string và N là độ dài của string
        

    # O(K)
    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            char = word[i]
            child = node.children.get(char, None)
            if not child:
                child = TrieNode()
                node.children[char] = child
            node = child  
        node.finished = True
        
    # O(K)
    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            char = word[i]
            child = node.children.get(char, None)
            if not child:
                return False
            node = child
        return node.finished
        
    # O(K)
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            char = prefix[i]
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