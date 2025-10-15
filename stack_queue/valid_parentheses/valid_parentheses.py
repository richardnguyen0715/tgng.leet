class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        parenthesis = {
            '{' : '}',
            '(' : ')',
            '[' : ']'
        }

        from collections import deque
        stack = deque()

        for i in range(len(s)):
            if s[i] in parenthesis.keys():
                stack.append(s[i])
            if s[i] in parenthesis.values():
                if len(stack) > 0:
                    open_par = stack.pop()
                    if parenthesis[open_par] != s[i]:
                        return False
                else:
                    return False
        
        if len(stack) > 0:
            return False

        return True