import ast
from solutions import removeDuplicates


with open('input.txt', 'r') as file:
    nums = ast.literal_eval(file.readline())
    
result = removeDuplicates(nums)
print(result)

with open('output.txt', 'w') as file:
    file.write(str(result))