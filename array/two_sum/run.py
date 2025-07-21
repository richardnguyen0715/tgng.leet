import ast
from solutions import twoSum

with open('input.txt', 'r') as f:
    nums = ast.literal_eval(f.readline())
    target = int(f.readline())

result = twoSum(nums, target)
print(result)

with open('output.txt', 'w') as f:
    f.write(str(result))
    print(f"Output written to output.txt: {result}")