class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * 4
        dp[0] = dp[2] = -prices[0]
        for i in range(len(prices)):
            dp[0] = max([dp[0], -prices[i]])# First time that buy the stock
            dp[1] = max([dp[1], dp[0]+prices[i]])# First time that sell the stock 
            dp[2] = max(dp[2], dp[1]-prices[i] )# Second time that buy the stock
            dp[3] = max(dp[3], dp[2]+prices[i])# Second time that sell the stock
        return dp[3]
