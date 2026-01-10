from typing import List
from math import isqrt


# Time limit exceeded solution
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def find_divisors(num: int) -> List[int]:
            divisors = [1]
            for i in range(2, num + 1):
                if num % i == 0:
                    divisors.append(i)

            return divisors

        ans = 0
        for num in nums:
            divisors = find_divisors(num)
            if len(divisors) == 4:
                ans += sum(divisors)
        
        return ans
    
    
# Optimized solution with square root method
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def find_divisors(num: int) -> List[int]:
            divisors = []
            
            i = 1
            while i * i <= num:
                if num % i == 0:
                    divisors.append(i)
                    if ( i != int(num / i)):
                        divisors.append(int(num/i))
                i += 1

            return divisors

        ans = 0
        for num in nums:
            divisors = find_divisors(num)
            if len(divisors) == 4:
                ans += sum(divisors)
        
        return ans
    
    
# Precomputed sieve solution
def divisor_count_and_sum_sieve(N: int):
    divs_count = [0] * (N + 1)
    divs_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            divs_count[j] += 1
            divs_sum[j] += i
    return divs_count, divs_sum

divs_count, divs_sum = divisor_count_and_sum_sieve(int(1e5))

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if divs_count[num] == 4:
                ans += divs_sum[num]
        return ans
    
    

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            divs = list()
            sr = isqrt(n)
            for i in range(1, sr):
                q, r = divmod(n, i)
                divs += (q, i) * (r == 0)
                if len(divs) > 4:
                    break
            else:
                if sr ** 2 == n:
                    divs += sr,
                elif n % sr == 0:
                    divs += (sr, n // sr)
                if len(divs) != 4:
                    continue
                ans += sum(divs)    

        return ans