class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        # Method 1. Greedy Algorithm
        minPrice = float("inf")
        maxProfit = 0
        n = len(prices)
        for i in range(n):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i]- minPrice)
        return maxProfit
    
        # # Method 2.1. Dp using 2-D Array
        dp = [[0] * 2 for _ in range(len(prices))] 
        # dp[i][0]: does not holds the storck; dp[i][1] holds the stock
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[len(prices)-1][0]
        #return max(dp[len(prices)-1])
        '''
        # Method 2.2. Dp using 1-D Array with State Compresssion
        dp = [0] * 2
        # dp[0]: does not holds the storck; dp[1] holds the stock
        dp[0] = 0
        dp[1] = -prices[0]
        for i in range(1, len(prices)):
            dp[0] = max(dp[0], dp[1]+prices[i])
            dp[1] = max(dp[1], -prices[i])
        return dp[0]
        