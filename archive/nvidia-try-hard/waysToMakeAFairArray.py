from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
        n = len(nums)
        sumEven = sum([nums[i] for i in range(0, n, 2)])
        sumOdd = sum([nums[i] for i in range(1, n, 2)])
        
        print(sumEven, sumOdd)

        res = 0
        for i in range(n):
            tempEven, tempOdd = sumEven, sumOdd

            stillEven = sum([nums[k] for k in range(0, i, 2)])
            stillOdd = sum([nums[k] for k in range(1, i, 2)])

            # print("i: ", i)
            # print("keep: ", stillEven, stillOdd)

            remainEven = tempEven - stillEven
            remainOdd = tempOdd - stillOdd

            if i % 2 == 0:
                remainEven -= nums[i]
            else:
                remainOdd -= nums[i]

            # print("remain: ", remainEven, remainOdd)

            finalEven = stillEven + remainOdd
            finalOdd = stillOdd + remainEven

            # print("final: ", finalEven, finalOdd)

            if finalEven == finalOdd:
                res += 1
        
        return res


from typing import List


# Tránh TLE bằng cách sử dụng thêm prefix sum để tránh tính đi tính lại StillEven và StillOdd
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        sumEven = sum(nums[i] for i in range(0, n, 2))
        sumOdd = sum(nums[i] for i in range(1, n, 2))
        
        # prefixEven[i] = tổng các nums[k] chẵn với k < i
        # prefixOdd[i]  = tổng các nums[k] lẻ   với k < i
        prefixEven = [0] * (n + 1)
        prefixOdd = [0] * (n + 1)
        for i in range(n):
            prefixEven[i + 1] = prefixEven[i]
            prefixOdd[i + 1] = prefixOdd[i]
            if i % 2 == 0:
                prefixEven[i + 1] += nums[i]
            else:
                prefixOdd[i + 1] += nums[i]
        
        res = 0
        for i in range(n):
            tempEven, tempOdd = sumEven, sumOdd

            # phần giữ lại bên trái i
            stillEven = prefixEven[i]
            stillOdd = prefixOdd[i]

            # phần bên phải (trước khi xóa)
            remainEven = tempEven - stillEven
            remainOdd = tempOdd - stillOdd

            # xóa nums[i] khỏi tổng bên phải
            if i % 2 == 0:
                remainEven -= nums[i]
            else:
                remainOdd -= nums[i]

            # sau khi xóa, bên phải bị dịch trái 1 -> chẵn/lẻ đổi vai
            finalEven = stillEven + remainOdd
            finalOdd = stillOdd + remainEven

            if finalEven == finalOdd:
                res += 1
        
        return res
    
    
from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # Tổng chẵn/lẻ ban đầu (tương ứng với "bên phải" trước khi duyệt)
        evenRight = 0
        oddRight = 0
        for i, v in enumerate(nums):
            if i % 2 == 0:
                evenRight += v
            else:
                oddRight += v
        
        evenLeft = 0
        oddLeft = 0
        res = 0
        
        for i, v in enumerate(nums):
            # Bỏ phần tử nums[i] ra khỏi phía phải
            if i % 2 == 0:
                evenRight -= v
            else:
                oddRight -= v
            
            # Sau khi xóa nums[i]:
            # - Phần trái giữ nguyên chỉ số: evenLeft, oddLeft
            # - Phần phải đổi chẵn/lẻ: evenRight -> odd, oddRight -> even
            finalEven = evenLeft + oddRight
            finalOdd  = oddLeft  + evenRight
            
            if finalEven == finalOdd:
                res += 1
            
            # Thêm nums[i] vào phía trái để dùng cho i+1
            if i % 2 == 0:
                evenLeft += v
            else:
                oddLeft += v
        
        return res
    
    from typing import List


# Tối ưu nhất:
# curr_diff là tổng chẵn - tổng lẻ
# khi xóa nums[i] thì nếu là fair thì nums[i] phải đúng bằng curr_diff, vì khi xóa nums[i] thì phần bên phải
# của i dịch sang trái 1 làm chẵn lẻ đổi vai -> nums[i] chính là sumEven - sumOdd
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        ids_count = 0
        cur_diff = sum(nums[::2]) - sum(nums[1::2])
        for num in nums:
            if num == cur_diff:
                ids_count += 1
            # điều chỉnh lại expected curr_diff mới
            cur_diff = (num << 1) - cur_diff # tương đương với curr_diff(new) = 2 *num - curr_diff(old)
        return ids_count