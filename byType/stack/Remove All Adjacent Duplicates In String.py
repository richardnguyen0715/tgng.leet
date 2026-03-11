class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if not stack:
                stack.append(s[i])
            else:
                if stack[-1] == s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
        
        return "".join(stack) if stack else ""
