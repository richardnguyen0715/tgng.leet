class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Đếm số lần xuất hiện của mỗi ký tự
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        visited = set()
        stack = []  # Monotonic increasing stack
        
        for char in s:
            count[char] -= 1  # Giảm count vì đã xét ký tự này
            
            if char in visited:
                continue  # Đã có trong kết quả rồi
            
            # Loại bỏ ký tự lớn hơn nếu còn xuất hiện sau này
            while stack and stack[-1] > char and count[stack[-1]] > 0:
                removed = stack.pop()
                visited.remove(removed)
            
            stack.append(char)
            visited.add(char)
        
        return ''.join(stack)