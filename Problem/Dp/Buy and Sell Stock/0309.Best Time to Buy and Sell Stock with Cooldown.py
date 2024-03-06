class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [0] * 4
        dp[0] = -prices[0]
        for i in range(1, len(prices)):
            pre_dp0 = dp[0]
            pre_dp2 = dp[2]
            dp[0] = max(dp[0], dp[1]-prices[i], dp[3]-prices[i]) # Buy a stock
            dp[1] = max(dp[1], dp[3]) # stay not buying a stock and not selling a stock
            dp[2] = pre_dp0 + prices[i]# Sell a stock
            dp[3] = pre_dp2 # cooldown
        # print(dp)
        return max(dp[1], dp[2], dp[3])
