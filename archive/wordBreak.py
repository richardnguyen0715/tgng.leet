from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Gọi dp[i] là chọn cho vị trí thứ i đến n - 1 (s[i:n-1])
        # dp[0] là result

        # Time: O(N * N * N)
        # Space: O(N) - stack depth

        n = len(s)
        wordSet = set(wordDict)

        @lru_cache(None)
        def dp(i): # O(N)
            if i == n:
                return True
            
            for j in range(i, n): # O(N)
                word = s[i:j+1] # O(N)
                if word in wordSet and dp(j+1):
                    return True
                
            return False

        
        return dp(0)
    
    
    
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Gọi dp[i] là chọn cho vị trí thứ i đến n - 1 (s[i:n-1])
        # dp[0] là result

        # Time: O(N * N + |total length of words|)
        # Space: O(N + |total length of words|) - stack depth + the number of node in trie

        n = len(s)
        wordSet = set(wordDict)

        trieRoot = TrieNode()
        for word in wordDict:
            trieRoot.addWord(word)

        @lru_cache(None)
        def dp(i): # O(N)
            if i == n:
                return True
            
            trieCur = trieRoot
            for j in range(i, n): # O(N)
                c = s[j]
                if c not in trieCur.children: # O(1)
                    break
                
                trieCur = trieCur.children[c]
                if trieCur.isWord and dp(j+1): # O(1)
                    return True

            return False

        
        return dp(0)