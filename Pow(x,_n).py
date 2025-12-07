class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        res = 1
        s = abs(n)

        while s:
            if s & 1:
                res *= x
            x *= x
            s >>= 1
        return res if n >=0 else 1/res