import ast

with open("input.txt", 'r') as file:
    digits = ast.literal_eval(file.readline())
    
from solutions import plusOne

result = plusOne(digits)
print(result)

with open("output.txt", 'w') as file:
    file.write(str(result))