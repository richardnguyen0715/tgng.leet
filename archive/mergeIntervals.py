from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last = merged[-1] # Lấy ra phần tử cuối cùng trong intervals xem xem có overlap hay không

            if start <= last[1]: # Tức là start nằm trong đoạn last[1] -> có overlap
                last[1] = max(end, last[1]) # Lấy max là gì có thể end sẽ lớn hơn -> 2 trường hợp là A trước B và B trước A
            else:
                merged.append([start, end]) # Không overlap

        return merged



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def sol_overlap(interval_a, interval_b):
            
            if (interval_a[0] >= interval_b[0] and interval_a[0] <= interval_b[1]) or (interval_a[1] >= interval_b[0] and interval_a[1] <= interval_b[1]) or (interval_b[0] >= interval_a[0] and interval_b[0] <= interval_a[1]) or (interval_b[1] >= interval_a[0] and interval_b[1] <= interval_a[1]):
                return [min(interval_a + interval_b), max(interval_a + interval_b)]
            
            return []
        
        n = len(intervals)
        for i in range(0, n - 1):
            next_idx = min(n - 1, i + 1)
            if next_idx == i:
                continue
            # print(len(intervals))
            # print(f"i: {i}, next: {next_idx}")
            a = sol_overlap(intervals[i], intervals[next_idx])
            if len(a) > 0:
                intervals[i] = a
                del intervals[next_idx]
                n -= 1
                i = -1
                # print(f"Intervals: {intervals}")
                # print(f"Got overlapp - i: {i}, next: {next_idx}")

        return intervals
        