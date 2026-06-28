class Solution:
    def simplifyPath(self, path: str) -> str:
        
        pathList = path.split('/')
        print(pathList)

        res = []
        n = len(pathList)
        i = n - 1
        while i >= 0:
            if pathList[i] == '': 
                i -= 1
                continue

            if pathList[i] == '.':
                i -= 1
                continue
            
            if pathList[i] == '..':
                i -= 2
                continue
            
            res.append(pathList[i])
            i -= 1
        
        res = res[::-1]
        ans = "/".join(res)
        ans = '/' + ans
        return ans
    
    
class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split('/')
        stack = []
        
        for component in pathList:
            if component == '' or component == '.':
                # Bỏ qua empty string và current directory
                continue
            elif component == '..':
                # Go back - pop nếu stack không rỗng
                if stack:
                    stack.pop()
            else:
                # Thư mục/file hợp lệ
                stack.append(component)
        
        # Tạo kết quả
        return '/' + '/'.join(stack)