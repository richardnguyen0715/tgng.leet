class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        res = 0

        for char in s:
            if char == ')':
                if not stack:
                    res += 1
                else:
                    stack.pop()
            else:
                stack.append('(')

        res += len(stack)

        return res