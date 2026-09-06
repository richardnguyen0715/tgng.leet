# Sai hướng - không sliding window
class Solution01:
    def numDistinct(self, s: str, t: str) -> int:
        
        # Config
        ans = 0

        # Setup
        sList = list(s)
        tList = list(t)
        tSet = set(tList)
        
        # O(N) -> Notice: don't use "in" operator in string: O(N) -> O(N^2): Right
        filtered_sList = [x for x in sList if x in tSet]
        # print("filtered: ", filtered_sList)

        # # Sliding Window: Failed
        # start = 0
        
        # n = len(filtered_sList)
        # m = len(tList)

        # visited = {}

        # while start < n - m:
        #     if start != tList[0]:
        #         start += 1
        #         continue
            
        #     stackList = []
        #     posT = 0
        #     stack = []

        #     for end in range(start, n):
        #         char = filtered_sList[end]
        #         if char == tList[posT]:

        #             if char == stack[-1]:
        #                 stackList.append(stack)

        #             stack.append(char)

        #             if not stackList:
        #                 stackList.append(stack)
        #             else:
        #                 for stack in stackList:
        #                     stack.append(char)
                    
        #             posT += 1

        #     start += 1


        # DFS

        def dfs(current, posT, posS):
            pass

            # Dùng backtracking để xét tất cả các trường hợp ghép các phần tử để tránh bỏ xót các phần tử nhảy cóc
            

# Dùng DFS - nhưng mà TLE rồi
class Solution02:
    def numDistinct(self, s: str, t: str) -> int:

        def dfs(posS, posT):
            if posT == len(t):
                return 1

            if posS == len(s):
                return 0

            ans = 0

            for i in range(posS, len(s)):
                if s[i] == t[posT]:
                    ans += dfs(i + 1, posT + 1)

            return ans

        return dfs(0, 0)
    
    
# Dùng DFS với mem, nhưng vẫn TLE
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        memo = {}

        def dfs(posS, posT):

            if posT == len(t):
                return 1

            if posS == len(s):
                return 0

            if (posS, posT) in memo:
                return memo[(posS, posT)]

            ans = 0

            for i in range(posS, len(s)):
                if s[i] == t[posT]:
                    ans += dfs(i + 1, posT + 1)

            memo[(posS, posT)] = ans

            return ans

        return dfs(0, 0)
    

# Dùng DP
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        n = len(s)
        m = len(t)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                # Don't use s[i - 1]
                dp[i][j] = dp[i - 1][j]

                # Use s[i - 1]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[n][m]