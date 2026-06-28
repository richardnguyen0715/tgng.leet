import ast
from solutions import findMedianSortedArrays


with open('input.txt', 'r') as file:
    nums1 = ast.literal_eval(file.readline())
    nums2 = ast.literal_eval(file.readline())
    
    
result = findMedianSortedArrays(nums1, nums2)
print(result)

with open('output.txt', 'w') as file:
    file.write(str(result))