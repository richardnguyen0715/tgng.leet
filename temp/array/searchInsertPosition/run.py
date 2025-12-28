import ast
from solutions import searchInsert


with open('input.txt', 'r') as file:
    nums = ast.literal_eval(file.readline())
    val = ast.literal_eval(file.readline())
    
result = searchInsert(nums, val)
print(result)

with open('output.txt', 'w') as file:
    file.write(str(result))