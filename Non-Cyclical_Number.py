class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num: int) -> int:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        
        seen = []
        
        while n != 1 and n not in seen:
            seen.append(n)
            n = get_next(n)
        
        return n == 1 