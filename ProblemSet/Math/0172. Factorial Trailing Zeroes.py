class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        '''
        for i in range(5, n+1, 5):
            while i % 5 == 0:
                i //= 5
                res += 1
        return res
        '''
        while n:
            n //= 5
            res += n
        return res
