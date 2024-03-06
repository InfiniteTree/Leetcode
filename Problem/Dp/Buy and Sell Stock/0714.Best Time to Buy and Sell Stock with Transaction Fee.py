class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [0] * 2
        dp[0] = -prices[0]-fee
        for i in range(1, len(prices)):
            dp[0] = max(dp[0],dp[1]-prices[i]-fee) # Buy a stock
            dp[1] = max(dp[1],dp[0]+prices[i])# Sell the stock
        return dp[1]
