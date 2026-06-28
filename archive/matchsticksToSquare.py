from typing import List



# Time Limit Exceeded -> O(4^N)
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        if sum(matchsticks) % 4 > 0:
            return False
        
        side_len = sum(matchsticks) // 4
        for i in matchsticks:
            if i > side_len:
                return False

        n = len(matchsticks)
        sum_on_side = [0] * 4
        ans = False
        matchsticks.sort(reverse=True)

        def choose(i):
            nonlocal ans
            # Chọn cạnh cho que thứ i
            if i == n:
                if all([k == side_len for k in sum_on_side]):
                    ans = True
                return
            
            for side in range(4):
                sum_on_side[side] += matchsticks[i]
                choose(i + 1)
                sum_on_side[side] -= matchsticks[i]

            
        choose(0)
        return ans


        
        
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        if sum(matchsticks) % 4 > 0:
            return False
        
        side_len = sum(matchsticks) // 4
        
        matchsticks.sort(reverse=True) # Lấy lớn nhất lên đầu tiên để check
        for i in matchsticks:
            if i > side_len:
                return False

        n = len(matchsticks)
        sum_on_side = [0] * 4
        ans = False
        

        def choose(i):
            nonlocal ans
            # Chọn cạnh cho que thứ i
            if i == n:
                if all([k == side_len for k in sum_on_side]):
                    ans = True
                return
            
            for side in range(4):
                
                if sum_on_side[side] + matchsticks[i] <= side_len:
                
                    sum_on_side[side] += matchsticks[i]
                    choose(i + 1)
                    sum_on_side[side] -= matchsticks[i]

            
        choose(0)
        return ans


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        if sum(matchsticks) % 4 > 0:
            return False
        
        side_len = sum(matchsticks) // 4
        
        matchsticks.sort(reverse=True) # Lấy lớn nhất lên đầu tiên để check
        
        if matchsticks[-1] + matchsticks[-2] > sum(matchsticks) // 2:
            return False
        
        for i in matchsticks:
            if i > side_len:
                return False

        n = len(matchsticks)
        sum_on_side = [0] * 4
        ans = False
        

        def choose(i):
            nonlocal ans
            # Chọn cạnh cho que thứ i
            if i == n:
                if all([k == side_len for k in sum_on_side]):
                    ans = True
                return
            
            for side in range(4):
                
                if sum_on_side[side] + matchsticks[i] <= side_len:
                
                    sum_on_side[side] += matchsticks[i]
                    choose(i + 1)
                    sum_on_side[side] -= matchsticks[i]

            
        choose(0)
        return ans
        
        

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        # Time: O(4^N)
        # Space: O(N)

        if sum(matchsticks) % 4 > 0:
            return False
        
        side_len = sum(matchsticks) // 4
        
        matchsticks.sort(reverse=True) # Lấy lớn nhất lên đầu tiên để check
        
        if len(matchsticks) >= 2:
            if matchsticks[-1] + matchsticks[-2] > sum(matchsticks) // 2:
                return False
        
        for i in matchsticks:
            if i > side_len:
                return False

        n = len(matchsticks)
        sum_on_side = [0] * 4
        ans = False
        

        def choose(i):
            nonlocal ans
            # Chọn cạnh cho que thứ i
            if i == n:
                if all([k == side_len for k in sum_on_side]):
                    ans = True
                return
            
            for side in range(4):
                
                # Bằng thì không nói, và thêm một trường hợp là nếu như bé hơn thì khi cộng thêm cũng sẽ phải bé hơn độ dài tối đa trừ đi thằng mới nhất (do đã được sort lớn đến bé nên  mới mất luôn là lớn nhất)
                if sum_on_side[side] + matchsticks[i] == side_len or sum_on_side[side] + matchsticks[i] <= side_len - matchsticks[-1]:
                
                    sum_on_side[side] += matchsticks[i]
                    choose(i + 1)
                    sum_on_side[side] -= matchsticks[i]

                    if ans:
                        return

            
        choose(0)
        return ans
        
        
        