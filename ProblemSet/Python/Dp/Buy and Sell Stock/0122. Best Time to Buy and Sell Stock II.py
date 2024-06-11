class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        minPrice = float("inf")
        maxProfit = 0
        n = len(prices)
        for i in range(n):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i]- minPrice)
        return maxProfit
        '''
        # Method 2. Dp
        dp = [0] * 2
        dp[0] = 0 # Does not hold the stock
        dp[1] = -prices[0] # Holds the stock
        for i in range(1, len(prices)):
            dp[0] = max(dp[0], dp[1]+prices[i])
            dp[1] = max(dp[1], dp[0]-prices[i])
        return dp[0]
        '''
        # Method 3. Greedy
        res = 0
        for i in range(1, len(prices)):
            res += max(prices[i]-prices[i-1], 0)
        return res
        '''
