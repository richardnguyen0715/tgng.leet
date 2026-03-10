from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        Use min-heap to efficiently find k smallest pairs.
        
        Strategy:
        1. Start with pairs (nums1[0], nums2[0]), (nums1[0], nums2[1]), ..., (nums1[0], nums2[k-1])
        2. When we pop (nums1[i], nums2[j]), we push (nums1[i+1], nums2[j]) if i+1 exists
        3. This ensures we explore pairs in order of increasing sum
        
        Time Complexity: O(k log k)
        Space Complexity: O(k)
        """
        if not nums1 or not nums2 or k == 0:
            return []
        
        result = []
        m, n = len(nums1), len(nums2)
        
        # Min-heap: (sum, i, j) where i is index in nums1, j is index in nums2
        heap = []
        
        # Initialize heap with first element of nums1 paired with first k elements of nums2
        # Why? nums1[0] + nums2[j] will always be smaller than nums1[i] + nums2[j] for i > 0
        for j in range(min(k, n)):
            heapq.heappush(heap, (nums1[0] + nums2[j], 0, j))
        
        # Extract k smallest pairs
        while heap and len(result) < k:
            current_sum, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            # If there's a next element in nums1, add the pair (nums1[i+1], nums2[j])
            # We only add the next i for the same j to avoid duplicates
            if i + 1 < m:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
        
        return result