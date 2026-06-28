class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # Time limit exceeded
        
        stack = []
        n = len(s)

        for i in range(n):
            if len(stack) >= k:
                flag = True # k thằng giống nhau
                stackSize = len(stack)
                for j in range(stackSize - k, stackSize):
                    if stack[j] == s[i - 1]:
                        continue
                    flag = False
                
                if flag == True:
                    for h in range(k):
                        stack.pop()
                
            stack.append(s[i])
            # print("i - stack: ", i, stack)

        if len(stack) >= k:
            flag = True # k thằng giống nhau
            stackSize = len(stack)
            for j in range(stackSize - k, stackSize):
                if stack[j] == s[i - 1]:
                    continue
                flag = False
            
            if flag == True:
                for h in range(k):
                    stack.pop()

        
        return "".join(stack) if stack else ""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # Time limit exceeded
        # Time: O(N*K)
        
        stack = []

        for char in s:
            stack.append(char)

            if len(stack) >= k and len(set(stack[-k:])) == 1:
                for _ in range(k):
                    stack.pop()
        
        return "".join(stack)


# Step	char	Stack (char, count)	            Action
# 1	    'd'	    [('d', 1)]	                    Push new
# 2	    'e'	    [('d', 1), ('e', 1)]	        Push new
# 3	    'e'	    [('d', 1), ('e', 2)]	        Increment
# 4	    'e'	    [('d', 1)]          	        Count=3, pop
# 5	    'd'	    [('d', 2)]	                    Increment
# 6	    'b'	    [('d', 2), ('b', 1)]	        Push new
# 7	    'b'	    [('d', 2), ('b', 2)]	        Increment
# 8	    'c'	    [('d', 2), ('b', 2), ('c', 1)]	Push new
# 9	    'c'	    [('d', 2), ('b', 2), ('c', 2)]	Increment
# 10	'c'	    [('d', 2), ('b', 2)]	        Count=3, pop
# 11	'c'	    [('d', 2), ('b', 2), ('c', 1)]	Push new
# 12	'b'	    [('d', 2), ('b', 3)]	        Increment
# 13	'd'	    [('d', 3)]	                    Increment
# 14	'a'	    [('a', 1)]	                    Push new
# 15	'a'	    [('a', 2)]	                    Increment
    
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Stack stores (character, consecutive_count)
        stack = []

        for char in s:

            if stack and stack[-1][0] == char:

                stack[-1][1] += 1

                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        result = []
        for char, count in stack:
            result.append(char * count)
        
        return "".join(result)