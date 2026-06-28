

# beat: 5% time, 5% space
class Solution:
    def isValid(self, word: str) -> bool:

        # Time Complexity: O(N)
        # Space: O(1)

        if len(word) < 3:
            return False

        vowel = [ord('a'), ord('o'), ord('e'), ord('u'), ord('i')]


        
        vowel_cnt = 0
        consonant_cnt = 0
        for character in word.lower():

            ascii_converted = ord(character)

            if (ascii_converted < ord('0')) or (ascii_converted > ord('9') and ascii_converted < ord('a'))or (ascii_converted > ord('z')):
                print(character, ascii_converted)
                print("out of range")
                return False

            if ascii_converted in vowel:
                vowel_cnt += 1
            
            if ord('a') <= ascii_converted <= ord('a') + 26 and ascii_converted not in vowel:
                consonant_cnt += 1
            
        if vowel_cnt < 1 or consonant_cnt < 1:
            print("vowel or consonant")
            return False
        
        return True
            


# Chuyển list vowel thành set để toán tử in thành O(1)
# Beat: 100% time, 10% space
class Solution:
    def isValid(self, word: str) -> bool:

        if len(word) < 3:
            return False

        vowel = set([ord('a'), ord('o'), ord('e'), ord('u'), ord('i')])
        
        vowel_cnt = 0
        consonant_cnt = 0
        for character in word.lower():

            ascii_converted = ord(character)

            if (ascii_converted < ord('0')) or (ascii_converted > ord('9') and ascii_converted < ord('a'))or (ascii_converted > ord('z')):
                print(character, ascii_converted)
                print("out of range")
                return False

            if ascii_converted in vowel:
                vowel_cnt += 1
            
            if ord('a') <= ascii_converted <= ord('a') + 26 and ascii_converted not in vowel:
                consonant_cnt += 1
            
        if vowel_cnt < 1 or consonant_cnt < 1:
            print("vowel or consonant")
            return False
        
        return True
            

            


        


        