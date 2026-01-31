from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        ans = "{" # because this is the first character greater than 'z'
        for letter in letters:
            if letter > target:
                ans = min(ans, letter)
        
        if ans != '{':
            return ans
        
        return letters[0]
                