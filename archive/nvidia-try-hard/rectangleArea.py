class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        overlap_x1 = max(ax1, bx1)
        overlap_y1 = max(ay1, by1)
        
        overlap_x2 = min(ax2, bx2)
        overlap_y2 = min(ay1, ay2)
        
        overlapArea = 0
        if overlap_x1 < overlap_x2 and overlap_y1 < overlap_y2:
            overlapArea = (overlap_x2 - overlap_x1) * (overlap_y2 - overlap_y1)
        
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - overlapArea