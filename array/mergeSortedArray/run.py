import ast

with open("input.txt", 'r') as file:
    nums1= ast.literal_eval(file.readline())
    m = ast.literal_eval(file.readline())
    nums2 = ast.literal_eval(file.readline())
    n = ast.literal_eval(file.readline())

from solutions import merge

result = merge(nums1, m, nums2, n)
print(result)

with open("output.txt", 'w') as file:
    file.write(str(result))