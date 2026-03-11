import itertools



class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        strN = list(str(n))
        permutations = list(itertools.permutations(strN))
        permutationList = list(set([int("".join(permu)) for permu in permutations]))
        permutationList.sort()

        for i in range(len(permutationList)):
            if permutationList[i] == n:
                
                if i == len(permutationList) - 1:
                    return -1
                
                return permutationList[i + 1] if permutationList[i + 1] <= 2 ** 31 -1 else -1
        


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Chuyển số thành list các chữ số
        digits = list(str(n))
        length = len(digits)
        
        # Bước 1: Tìm pivot - chữ số đầu tiên (từ phải sang trái) mà digits[i] < digits[i+1]
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        
        # Nếu không tìm thấy pivot → array giảm dần → không có next greater
        if i == -1:
            return -1
        
        # Bước 2: Tìm successor - chữ số nhỏ nhất bên phải lớn hơn digits[i]
        j = length - 1
        while j > i and digits[j] <= digits[i]:
            j -= 1
        
        # Bước 3: Swap pivot và successor
        digits[i], digits[j] = digits[j], digits[i]
        
        # Bước 4: Reverse phần từ i+1 đến cuối
        digits[i + 1:] = reversed(digits[i + 1:])
        
        # Chuyển về số nguyên
        result = int(''.join(digits))
        
        # Bước 5: Check 32-bit integer constraint
        return result if result <= 2**31 - 1 else -1