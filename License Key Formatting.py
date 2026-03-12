class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        res = []
        count = 0

        # reverse là do để thằng đầu tiên sẽ group những thằng còn lại nếu như ko đủ k phần tử
        for char in reversed(s):
            if char == '-':
                continue
            
            if count == k:
                res.append('-')
                count = 0
            
            res.append(char.upper())
            count += 1
        
        return "".join(reversed(res))