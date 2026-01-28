

# Beat: 35% Time, 12% Space
class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        # Time: O(N * (Log10(N) + 1)), trong đó Log10N + 1 là số chữ số của phần tử lớn nhất
        # Space: O(1)
        
        good_digit = {'0', '1', '2', '5', '8', '6', '9'}

        rotated_map = {
            '0' : '0',
            '1' : '1',
            '2' : '5',
            '5' : '2',
            '8' : '8',
            '6' : '9',
            '9' : '6'
        }

        def checkRotated(digits):
            res = []
            for char in digits:
                if char not in good_digit:
                    return False
                
                res.append(rotated_map[char])
            
            return "".join(res) != digits
                
        cnt = 0
        for i in range(n + 1):
            if checkRotated(str(i)):
                print(i)
                cnt += 1
        
        return cnt
            