class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = dp[1] = 0
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i): # i/2 due to cauchy inequality
                dp[i] = max(j*(i-j), j*dp[i-j], dp[i])
        return dp[-1]
