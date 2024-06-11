class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        dp = [[0] *(n+1) for _ in range(k+1)]
        for i in range(1, k+1):
            dp[i][i-1] = mx = -inf
            w = (1 if i % 2 else -1) * (k-i+1)
            for j in range(i, n-k+i+1):
                mx = max(mx, dp[i-1][j-1] - s[j-1]*w)
                dp[i][j] = max(dp[i][j-1], s[j]*w+mx)
        return dp[k][n]
