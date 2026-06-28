class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split(" ")
        resList = [word for word in sList if word != ""]
        print(resList)
        return " ".join(resList[::-1])