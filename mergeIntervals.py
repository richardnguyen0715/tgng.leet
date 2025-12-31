from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last = merged[-1]

            if start <= last[1]:  # overlap
                last[1] = max(last[1], end)
            else:
                merged.append([start, end])

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
        