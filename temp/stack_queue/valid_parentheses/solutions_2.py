class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        parentheses = {
            '{' : '}',
            '(' : ')',
            '[' : ']'
        }

        stack = []

        for i in range(len(s)):
            if s[i] in parentheses.keys():
                stack.append(s[i])
            if s[i] in parentheses.values():
                if len(stack) == 0:
                    return False
                if parentheses[stack[-1]] != s[i]:
                    return False
                stack.pop()

        return len(stack) == 0