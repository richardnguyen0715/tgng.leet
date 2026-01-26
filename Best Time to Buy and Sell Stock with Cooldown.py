class Solution:
    def maxProfit(self, prices):
        
        # Time: O(n)
        # Space: O(n)
        
        if len(prices) <= 1:
            return 0
        
        n = len(prices)
        
        # Khởi tạo ngày 0
        hold = [-prices[0]]  # Mua ngày 0
        sold = [0]           # Không thể bán ngày 0
        rest = [0]           # Không làm gì ngày 0
        
        for i in range(1, n):
            # Trạng thái hold ngày i
            hold.append(max(hold[i-1], rest[i-1] - prices[i]))
            
            # Trạng thái sold ngày i  
            sold.append(hold[i-1] + prices[i])
            
            # Trạng thái rest ngày i
            rest.append(max(rest[i-1], sold[i-1]))
        
        # Kết quả tối ưu: không nắm giữ cổ phiếu ở cuối
        return max(sold[-1], rest[-1])
    
   
   
# Space optimized
# Time: O(N)
# Space: O(1)

def maxProfit(prices):
    if len(prices) <= 1:
        return 0
    
    hold = -prices[0]  # Chỉ cần lưu giá trị hiện tại
    sold = 0
    rest = 0
    
    for i in range(1, len(prices)):
        prev_hold = hold
        prev_sold = sold
        prev_rest = rest
        
        hold = max(prev_hold, prev_rest - prices[i])
        sold = prev_hold + prices[i]
        rest = max(prev_rest, prev_sold)
    
    return max(sold, rest)