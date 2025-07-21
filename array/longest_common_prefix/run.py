import ast
from solutions import longestCommonPrefix

with open("input.txt", 'r') as f:
    strs = ast.literal_eval(f.readline())
    
resutls = longestCommonPrefix(strs)
print(resutls)

with open("output.txt", 'w') as f:
    f.write(str(resutls))