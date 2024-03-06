class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [0] * (2*k+1) 
        for i in range(1, 2*k+1, 2):
            dp[i] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(1, 2*k+1):
                if j % 2 == 1:
                    dp[j] = max(dp[j], dp[j-1]-prices[i]) # dp[2c+1] buy the stock
                else:
                    dp[j] = max(dp[j], dp[j-1]+prices[i]) # dp[2m] sell the stock
            #print(dp)
        return dp[-1]
