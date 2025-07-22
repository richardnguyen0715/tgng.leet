with open("input.txt", 'r') as f:
    roman = str(f.readline())
    
from solutions import romanToInt

res = romanToInt(roman)
print(res)

with open("output.txt", "w") as f:
    f.write(str(res))