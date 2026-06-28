from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq


        pool = []

        for idx, point in enumerate(points):
            pool.append((self.get_distance(point), idx))

        heapq.heapify(pool)
        ans = []
        for i in range(0, k):
            point = heapq.heappop(pool)
            ans.append(points[point[1]])

        return ans
        

    def get_distance(self, p1):
        return p1[0] * p1[0] + p1[1] * p1[1]