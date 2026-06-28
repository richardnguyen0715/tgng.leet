from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
    
        maxProfit = 0
        minPrice = prices[0]
        
        # Chỉ cần biết min price trước đó là gì thôi vì cơ bản vòng for luôn chạy tới thời điểm tiếp theo rồi
        for price in prices:
            minPrice = min(price, minPrice)
            maxProfit = max(maxProfit, price - minPrice)
        
        return maxProfit
    
    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        n = len(prices)
        
        # Dynamic Programming:
        # Có thể có 2 trạng thái cố định độc lập nhau tại mỗi bước di chuyển
        # Gọi dp[i][0] là lợi nhuận tối đa tại ngày thứ i nếu như không nắm giữ cổ phiếu
            # Trường hợp 1: hôm trước cũng không mua
            # Trường hợp 2: hôm nay bán
        # Gọi dp[i][1] là lợi nhuận tối đa tại ngày thứ i nếu như nắm giữ cổ phiếu
            # Trường hợp 1: hôm tước đã mua rồi
            # Trường hợp 2: hôm nay mua ( chỉ mua một lần )
        
        dp = [[0, 0] for _ in range(n)]
        
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        
        return dp[n-1][0]
    
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
                
        if not prices:
            return 0
        
        n = len(prices)
        
        # Tối ưu thêm không gian bằng cách chỉ lưu trạng thái của ngày trước đó
        hold = -prices[0]
        sold = 0

        for i in range(1, n):
            new_sold = max(sold, prices[i] + hold) # Bán hoặc không làm gì
            new_hold = max(hold, -prices[i]) # Giữ hoặc mua mới

            sold = new_sold
            hold = new_hold
        
        return sold