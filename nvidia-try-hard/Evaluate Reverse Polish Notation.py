from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        operations = ['+', '-', '*', '/']
        def calculator(a, b, token):
            if token == '+':
                return a + b
            
            if token == '-':
                return a - b

            if token == '*':
                return a * b
            
            if token == '/':
                return int(a / b)

        for token in tokens:
            if token not in operations:
                stack.append(token)
            else:
                a = stack.pop()
                b = stack.pop()
                c = str(calculator(int(b), int(a), token))
                stack.append(c)
        
        # print(stack)
        return int(stack.pop())
        