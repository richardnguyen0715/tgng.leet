import ast
from solutions import isPalindrome

with open('input.txt', 'r') as f:
    x = ast.literal_eval(f.readline())
    
res = isPalindrome(x)
print(res)

with open('output.txt', 'w') as f:
    f.write(str(x))