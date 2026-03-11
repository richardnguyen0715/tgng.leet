class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        res = []
        depth = 0

        for char in s:
            if char == "(":
                if depth > 0:
                    res.append(char)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    res.append(char)
        
        return "".join(res)


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        stack = []
        
        for char in s:
            if char == '(':
                # If stack is not empty, this '(' is not outer
                if stack:
                    result.append(char)
                stack.append(char)
            else:  # char == ')'
                stack.pop()
                # If stack is not empty after popping, this ')' is not outer
                if stack:
                    result.append(char)
        
        return ''.join(result)