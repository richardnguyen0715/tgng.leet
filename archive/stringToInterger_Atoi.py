class Solution:
    def myAtoi(self, s: str) -> int:

        if len(s) == 0:
            return 0

        # Remove white space
        left = 0
        n = len(s)
        while left < n and s[left] == " ":
            left += 1

        if left >= n:
            return 0

        sign = 1
        if s[left] == "-":
            sign = -1
            left += 1
        
        elif s[left] == "+":
            left += 1
        
        if left >= n:
            return 0
        
        int_char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        if s[left] not in int_char:
            return 0
        
        while left < n and s[left] == "0":
            left += 1
        print("left", left)

        right = left
        while right < n and s[right] in int_char:
            right += 1
        print("right", right)

        res = sign * int(s[left:right]) if left != right else 0

        if res < (-1) * pow(2, 31):
            res = (-1) * pow(2, 31)
        elif res > pow(2, 31) - 1:
            res = pow(2, 31) - 1


        # print(s[left:right])
        return res
        

        





            
        
