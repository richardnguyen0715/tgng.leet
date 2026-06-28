from typing import List


# Approach này bị sai, do không có tính partition
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = set()
        candidates = list(s)

        def isPalindrome(a):
            if len(a) == 1:
                return True
            
            left = 0
            right = len(a) - 1
            while left < right:
                if a[left] != a[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True

        def merge_element(arr, i , j):
            if i > j and i < 0 or j >= len(arr):
                return arr

            merged = "".join(arr[i:j+1])

            return arr[:i] + [merged] + arr[j+1:]

        print("candidates list: ", candidates)
        for i in range(n):
            for j in range(i, n):
                candidate = "".join(candidates[i:j+1])
                print("candidate: ", candidate)
                if isPalindrome(candidate):
                    ans = merge_element(candidates, i , j)
                    print("merged: ", ans)
                    result.add(tuple(ans))
                    print("current res: ", result)

        return [list(res) for res in result]



# Approach DFS - backtracking:
# Time: O(2^N * N) - 2^N cách tạo partition, N check palindrome
# Space: O(N^2) - Palindrome table, O(N) cho recursion stack 
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # Ý tưởng: bài này cần tìm tất cả các partition có thể có của substring

        n = len(s)

        def isPalindrome(string, left, right):
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        results = []
        current_partition = []

        def dfs(start):
            # Chọn partition cho vị trí thứ i
            if start == n: # Tức là chọn xong tới vị trí cuối cùng rồi
                results.append(current_partition.copy())
                return
            
            for end in range(start, n):
                if isPalindrome(s, start, end):
                    current_partition.append(s[start:end+1])

                    # Tới partition tiếp theo
                    dfs(end + 1)

                    current_partition.pop()

                
        dfs(0)
        return results