from collections import deque

class Solution:
    
    # Time limit exceeded
    def minFlips(self, s: str) -> int:
        
        n = len(s)
        dq = deque(s)
        res = float("inf")
        
        for _ in range(n):
            
            countType1 = 0  # 101010...
            countType2 = 0  # 010101...
            
            for i in range(n):
                
                # pattern: 101010...
                if (i % 2 == 0 and dq[i] != '1') or (i % 2 == 1 and dq[i] != '0'):
                    countType1 += 1
                
                # pattern: 010101...
                if (i % 2 == 0 and dq[i] != '0') or (i % 2 == 1 and dq[i] != '1'):
                    countType2 += 1
            
            res = min(res, countType1, countType2)
            
            # rotate
            dq.append(dq.popleft())
        
        return res
    
    

class Solution:
    def minFlips(self, s: str) -> int:
        
        # Phải thử hết các rotation cần thiết nữa -> hiện tại chỉ thử 1 rotation
        
        # 111000 : type 1 -> 110001 -> 100011 -> 101010
        # 111000 : type 2 -> 101010

        # constraint: len(s) >= 10 ^ 5 -> remove(recursive)

        # type 1: 1010101010...
        # type 2: 0101010101...

        sListType1 = deque(list(s))
        sListType2 = deque(list(s))

        n = len(s)
        countType1 = 0
        countType2 = 0

        while sListType1[1] != '0':
            sListType1.popleft()
            sListType1.append('1')
        print("1-type:", sListType1)
        for i in range(n):
            if i % 2 != 0 and sListType1[i] == '1':
                countType1 += 1
            if i % 2 == 0 and sListType1[i] == '0':
                countType1 += 1
        
        print("min-type1: ", countType1)
        
        while sListType2[1] != '1':
            sListType2.popleft()
            sListType2.append('0')
        print("0-type:", sListType2)
        for i in range(n):
            if i % 2 != 0 and sListType2[i] == '0':
                countType2 += 1
            if i % 2 == 0 and sListType2[i] == '1':
                countType2 += 1
        print("min-type2: ", countType2)
        
        return min(countType1, countType2)


class Solution:
    def minFlips(self, s: str) -> int:
        
        # 111000 : type 1 -> 110001 -> 100011 -> 101010
        # 111000 : type 2 -> 101010

        # constraint: len(s) >= 10 ^ 5 -> remove(recursive)

        # type 1: 1010101010...
        # type 2: 0101010101...

        # s = s + s -> 111000111000
        # 111000
        # 110001
        # 100011
        # 000111
        # 001110
        # 011100
        # Mỗi một case sinh ra từ s + s thì tiến hành so sánh với các pattern -> tìm ra diff với các pattern -> sau đó lấy min
        
        n = len(s)
        s = s + s

        pattern1 = []
        pattern2 = []

        for i in range(len(s)):
            if i % 2 == 0:
                pattern1.append("1")
                pattern2.append("0")
            else:
                pattern1.append("0")
                pattern2.append("1")
        
        diff1 = 0
        diff2 = 0
        left = 0
        res = float("inf")

        for right in range(len(s)):
            if s[right] != pattern1[right]:
                diff1 +=1
            if s[right] != pattern2[right]:
                diff2 +=1
            
            if right - left + 1 > n: # center
                if s[left] != pattern1[left]:
                    diff1 -= 1
                if s[left] != pattern2[left]:
                    diff2 -= 1
                left += 1
            
            if right - left + 1 == n:
                res = min(res, diff1, diff2)
        
        return res
