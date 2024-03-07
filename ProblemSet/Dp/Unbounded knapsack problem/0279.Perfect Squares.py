class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        squares = [i*i for i in range(1, int(n**0.5)+1)]
        for square in squares:
            for j in range(square, n+1):
                dp[j] = min(dp[j], dp[j-square]+1)
        return dp[-1]
