class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n) # tối đa sẽ có m + n chữ số
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])

                # vị trí của biến carry (p1) và vị trí hiện tại (p2)
                p1, p2 = i + j, i + j + 1

                total = mul + result[p2]
                # Hiện tại
                result[p2] = total % 10

                # Carry +=
                result[p1] += total // 10

        # Skip leading zeros
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
        
        return ''.join(map(str, result[start:]))