

class Solution:
    def minimumDistance(self, word: str) -> int:
        
        def init():    
        
            charMatrix = [
                ["A", "B", "C", "D", "E", "F"]
                ["G", "H", "I", "J", "K", "L"]
                ["M", "N", "O", "P", "Q", "R"]
                ["S", "T", "U", "V", "W", "X"]
                ["Y", "Z", "", "", "", ""]
            ]
            
            # charToPos = {}
            # for i in range(len(charMatrix)):
            #     for j in range(len(charMatrix[0])):
            #         char = charMatrix[i][j]
            #         if char:
            #             charToPos[char] = (i ,j)
            
            # return charToPos
            
            pos = [None] * 26

            for i in range(len(charMatrix)):
                for j in range(len(charMatrix[i])):
                    char = charMatrix[i][j]
                    if char:
                        pos[ord(char) - ord('A')] = (i, j)
            
            return pos
            
        def getIndex(pos, char):
            return pos[ord(char) - ord('A')]
                
        def getDistance(x, y):
            if not x or not y:
                return 0
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        pos = init()
        n = len(word)
        
        # SOLUTION 1: Centroid
        # Tính từ chữ cái -> khoảng cách ngắn nhất đên 2 ngón tay!!! -> ngón nào ngắn hơn thì lấy ngón đó?
        # Note: Làm sao để biết mà gán cho fingers? -> nếu finger None thì lấy ngón nào nằm ở trung tâm!! -> tức là ngón đó cách các ngón khác gần nhất?   

        # Tuy nhiên cách này cũng sai -> vì các ngón tay động!!! -> chắc gì sau đó thì còn min?
            # Giải pháp là xoay vòng tìm centroids? -> cũng không phải! -> do vì các centroids sẽ liên tục động -> không hội tụ. Ngoài ra cost tính bị sai
            # Min distance phụ thuộc vào kí tự sắp tới và vị trí của ngón tay trước đó -> phụ thuộc vào bước trước đó 

        # charPos = [getIndex(pos, c) for c in word]
        # min_cost = float('inf')
        # best_pair = None

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         cost = 0
        #         for k in range(n):
        #             d1 = getDistance(charPos[k], charPos[i])
        #             d2 = getDistance(charPos[k], charPos[j])
        #             cost += min(d1, d2)
                
        #         if cost < min_cost:
        #             min_cost = cost
        #             best_pair = (i, j)
        
        # fingers = [
        #     charPos[best_pair[0]],
        #     charPos[best_pair[1]]
        # ]
        
        
        # SOLUTION 2: Dynamic programming
        
        # Sau khi gõ word[i] thì một trong 2 ngón chắc chắn đang ở word[i] -> ngón còn lại mới là ngón chưa biết
        # -> chỉ cần xét dp[i][j] , tại i thì một ngón chắc chắn đang ở word[i], j là vị trí của ngón còn lại
        # Chi phí nhỏ nhất để gõ từ 0 -> i với 1 ngón ở word[i], một ngón ở vị trí j
        
        dp = {}
        dp = [(None, None)] = 0
        for c in word:
            next_dp = {}
            pos_c = getIndex(c)
            
            for (f1, f2), cost in dp.items():
                
                # di chyyển f1 đến c
                newCost = cost + getDistance(f1, pos_c)
                key = (pos_c, f2)
                next_dp[key] = min(next_dp.get(key, float("inf")), newCost)
                
                # di chuyển từ f2 đến c
                newCost = cost + getDistance(f2, pos_c)
                key = (f1, pos_c)
                next_dp[key] = min(next_dp.get(key, float("inf")), newCost)
            
            dp = next_dp
        
        return min(dp.values())