class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # n: độ dài string
        # m: độ dài pattern
        n = len(s)
        m = len(p)

        # dp[i][j] = True nếu:
        # s[0:i] (prefix dài i của s)
        # match với
        # p[0:j] (prefix dài j của p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # base case:
        # empty string match empty pattern
        dp[0][0] = True

        # xử lý trường hợp string rỗng nhưng pattern không rỗng
        # ví dụ pattern: a*, a*b*, a*b*c*
        # vì '*' cho phép lặp 0 lần
        for j in range(2, m + 1):
            if p[j - 1] == '*':
                # bỏ cặp (char + *)
                dp[0][j] = dp[0][j - 2]

        # duyệt từng prefix của string
        for i in range(1, n + 1):

            # duyệt từng prefix của pattern
            for j in range(1, m + 1):

                # CASE 1: ký tự pattern không phải '*'
                if p[j - 1] != '*':

                    # kiểm tra ký tự có match không
                    # match nếu:
                    # - giống nhau
                    # - pattern là '.'
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':

                        # nếu match thì phụ thuộc vào trạng thái trước đó
                        # bỏ cả 2 ký tự
                        dp[i][j] = dp[i - 1][j - 1]

                # CASE 2: gặp '*'
                else:

                    # '*' luôn đi kèm ký tự trước đó
                    # ví dụ a*
                    # lựa chọn 1: dùng 0 lần
                    # bỏ cặp (char + *)
                    dp[i][j] = dp[i][j - 2]

                    # lựa chọn 2: dùng >= 1 lần
                    # chỉ hợp lệ nếu ký tự trước '*' match với s[i-1]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':

                        # nếu match thì:
                        # tiêu thụ thêm 1 ký tự của s
                        # nhưng vẫn giữ pattern ở j
                        dp[i][j] |= dp[i - 1][j]

        # kết quả cuối cùng:
        # toàn bộ s match toàn bộ p
        return dp[n][m]
    
    

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # TopDown DP
        # Time: O(MxN)
        # Space: O(MxN)
        
        # dp[i][j] là s[i:] có match với p[j:] hay không, basecase là dp[m][n] = True vì "" match ""

        memo = {}

        def dp(i, j):

            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            first_match = (
                i < len(s) and
                (p[j] == s[i] or p[j] == '.')
            )

            if j + 1 < len(p) and p[j+1] == '*':
                ans = (
                    dp(i, j+2) or
                    (first_match and dp(i+1, j))
                )
            else:
                ans = first_match and dp(i+1, j+1)

            memo[(i, j)] = ans
            return ans

        return dp(0,0)