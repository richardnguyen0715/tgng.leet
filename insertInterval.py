from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval) # Time: O(1)
        intervals.sort(key=lambda x: x[0]) # Time: O(NLogN), Space: O(N)
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last = merged[-1] # Lấy ra phần tử cuối cùng trong intervals xem xem có overlap hay không

            if start <= last[1]: # Tức là start nằm trong đoạn last[1] -> có overlap
                last[1] = max(end, last[1]) # Lấy max là gì có thể end sẽ lớn hơn -> 2 trường hợp là A trước B và B trước A
            else:
                merged.append([start, end]) # Không overlap

        return merged
            

            

