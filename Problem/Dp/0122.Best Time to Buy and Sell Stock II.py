class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        maxProfit = 0
        n = len(prices)
        for i in range(n):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i]- minPrice)
        return maxProfit
    