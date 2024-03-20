class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        res = 1
        if n < 0:
            x, n = 1/x, -n
        while n:
            if n & 1: # n % 2 == 1
                res *= x
            x *= x # x **= 2
            n >>= 1 # n // = 2
        return res
