from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums:
            return []

        res = []
        n = len(nums)
        start = nums[0]
        current = start
        for i in range(1, n):
            current += 1
            end = nums[i]
            print(current, end)
            if current != end:
                if nums[i - 1] != start:
                    res.append(f"{start}->{nums[i - 1]}")
                else:
                    res.append(f"{start}")

                start = end
                current = start
                print("---")
                print(current, start)


        # Thêm vào khúc cuối của dãy
        if current != start:
            res.append(f"{start}->{current}")
        else:
            res.append(f"{start}")
        

        return res