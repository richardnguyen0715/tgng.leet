class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        """
            [3,2,4,1]
            1. 4, 2, 3, 1 (3) -> 1, 3, 2, 4 (4)
            2. 3, 1, 2, 4 (2) -> 2, 1, 3, 4 (3)
            3. 2, 1, 3, 4 (1) -> 1, 2, 3, 4 (2)
            => Results: [3,4,2,3,1,2]
        """
        n = len(arr)
        count = n - 1
        results = []
        while (count > 0):
            maxIndex = count
            for i in range(0, count):
                if arr[maxIndex] < arr[i]:
                    maxIndex = i
            results.append(maxIndex + 1)
            arr = self.flip(arr, maxIndex + 1) # Đưa số lớn nhất về đầu tiên bằng flip
            results.append(count + 1)
            arr = self.flip(arr, count + 1) # Đưa số lớn nhất về cuối bằng flip tại count
            count -= 1
        return results
        
    def flip(self, arr, k):
        left = 0
        right = k - 1
        while left < right:
            arr = self.swap(arr, left, right)
            left += 1
            right -= 1
        return arr

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        return arr
        

