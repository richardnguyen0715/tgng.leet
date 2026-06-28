class Solution:
    def divide(self, dividend, divisor):
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        
        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign and work with positives
        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        result = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple
        
        result = -result if negative else result
        return max(INT_MIN, min(INT_MAX, result))