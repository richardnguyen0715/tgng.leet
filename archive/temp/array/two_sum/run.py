import ast
# from solutions import twoSum
from solutions_2 import twoSum

# with open('input.txt', 'r') as f:
#     nums = ast.literal_eval(f.readline())
#     target = int(f.readline())

nums = [2, 7, 8 , 9]
target = 9

result = twoSum(nums, target)
print(result)

with open('output.txt', 'w') as f:
    f.write(str(result))
    print(f"Output written to output.txt: {result}")