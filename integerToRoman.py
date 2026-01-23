class Solution:
    def intToRoman(self, num: int) -> str:
        
        #  Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
        convert_engine = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"),
            (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        res = []
        
        for val, roman in convert_engine:
            count = num // val # Chia lấy phần nguyên xem tối đa được bao nhiêu lần
            if count > 0:
                res.append(roman * count)
                num -= val * count

        return "".join(res)