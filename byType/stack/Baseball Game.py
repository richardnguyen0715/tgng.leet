from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for operation in operations:

            if operation == '+':
                x, y = int(stack[-1]), int(stack[-2])

                stack.append(x + y)
            
            elif operation == 'D':
                stack.append(2 * int(stack[-1]))

            elif operation == 'C':
                stack.pop()
            
            else:
                stack.append(int(operation))
        
        print(stack)
        
        return sum(stack)