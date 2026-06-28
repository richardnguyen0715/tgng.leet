class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0 :
            flag = True
        x = abs(x)
        str_x = str(x)
        reversed_str_x = str_x[::-1]
        if flag == True:
            new_x = (-1) * (int(reversed_str_x))
        else:
            new_x = int(reversed_str_x)

        if new_x < (-1) * pow(2, 31) or new_x > pow(2, 31) - 1:
            new_x = 0

        return new_x