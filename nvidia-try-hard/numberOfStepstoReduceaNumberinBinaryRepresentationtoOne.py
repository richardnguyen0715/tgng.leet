class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0

        # s[0] == 1 nên luôn bỏ qua bit đầu tiên
        for i in range(len(s) - 1, 0, -1):

            current_bit = int(s[i]) + carry

            if current_bit == 1: # số lẻ -> cần 2 bước
                steps += 2
                carry = 1
            else: # số chẵn -> carry = current_bit // 2
                steps += 1
                carry = current_bit // 2
            
        return steps + carry