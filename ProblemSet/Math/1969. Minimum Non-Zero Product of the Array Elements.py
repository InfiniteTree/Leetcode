class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        modulo = 10 ** 9 + 7
        # (2^p - 1) * (2^p - 2)^((2^(p-1))-1)
        k = (1 << p) - 1
        return k * pow(k-1, (k-1)>>1, modulo) % modulo
