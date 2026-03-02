from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort(reverse=True)

        # Tính từ lớn đến nhỏ: nếu số cite < số bài thì dừng, ngược lại thì cứ đi tiếp

        h = 0
        for i, cite in enumerate(citations):

            # i + 1 là số bài
            if cite >= i + 1:
                h = i + 1
            else:
                break
            
        return h