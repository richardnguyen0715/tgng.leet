from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        
        n = len(chars)
        s = ""
        start = 0
        end = 0
        
        while end < n:
            while end < n and chars[start] == chars[end]:
                end += 1
            groupCount = end - start
            print(start, end)

            if groupCount == 1:
                s += chars[start]
            else:
                s += chars[start]
                s += str(groupCount)

            start = end
        
        print(s)
        print(list(s))
        chars.clear()
        chars.extend(list(s))

        return len(s)
                

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        n = len(chars)
        s = []
        start = 0
        end = 0
        while end < n:
            while end < n and chars[start] == chars[end]:
                end += 1
            groupCount = end - start
            # print(start, end)

            if groupCount == 1:
                s.append(chars[start])
            else:
                s.append(chars[start])
                s.extend(list(str(groupCount)))

            start = end
        
        print(s)
        chars[:] = s

        return len(s)
                
            