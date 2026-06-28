class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stackS = []
        stackT = []

        for char in s:
            if stackS and char == '#':
                stackS.pop()
            else:
                if char != "#":
                    stackS.append(char)
        
        for char in t:
            if stackT and char == '#':
                stackT.pop()
            else:
                if char != "#":
                    stackT.append(char)

        print(stackS)
        print(stackT)
        
        return "".join(stackS) == "".join(stackT)
