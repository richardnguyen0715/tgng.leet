class Solution:
    def integerReplacement(self, n: int) -> int:
        
        cnt = 0
        
        while n > 1:
            if n % 2 == 0:
                n = int(n / 2)
            else:
                if n == 3: # special case
                    n -= 1
                elif (n & 3) == 1: # n % 4 == 1
                    n -= 1
                else:
                    n += 1


            cnt += 1
            print(n, " -> ", cnt)
        
        return cnt
                        
        