from typing import List

class Solution:
    def oddString(self, words: List[str]) -> str:
        n = len(words)
        m = len(words[0]) - 1
        differences = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                differences[i][j] = ord(words[i][j + 1]) - ord(words[i][j])
        
        hashMap = {}
        print(differences)
        for idx, difference in enumerate(differences):
            difference = tuple(difference)
            if difference not in hashMap:
                hashMap[difference] = [1, idx]
            else:
                hashMap[difference][0] += 1
                hashMap[difference][1] = idx

        print(hashMap)
            
        for key, val in hashMap.items():
            if val[0] == 1:
                return words[val[1]]