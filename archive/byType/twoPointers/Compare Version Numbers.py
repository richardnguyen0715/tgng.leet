class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        s1List = version1.split(".")
        s1List = [int(char) for char in s1List]
        s2List = version2.split(".")
        s2List = [int(char) for char in s2List]

        m, n = len(s1List), len(s2List)

        i = 0
        while i < m and i < n:
            if s1List[i] > s2List[i]:
                return 1
            elif s1List[i] < s2List[i]:
                return -1
            
            i += 1
        
        # print(m, n, i)

        if m == n:
            return 0

        if i == m:
            if sum(s2List[i:]) == 0:
                return 0
            return -1
        
        if i == n:
            if sum(s1List[i:]) == 0:
                return 0
            return 1

