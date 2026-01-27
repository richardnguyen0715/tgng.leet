class Solution:
    def greatestLetter(self, s: str) -> str:
        
        appeared = set()
        maxChar = ""
        for charac in s:
            
            appeared.add(charac)
            print(appeared)
            
            lower_char = charac.lower()
            upper_char = charac.upper()


            if lower_char in appeared and upper_char in appeared:
                print(maxChar, charac)
                maxChar = max(maxChar, charac.upper())
                print(maxChar)

        return maxChar.upper()


            