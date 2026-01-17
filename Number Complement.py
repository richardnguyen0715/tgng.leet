class Solution:
    def findComplement(self, num: int) -> int:

        for i in range(0, len(format(num, 'b'))):
            num = num ^ (1 << i)

        return num