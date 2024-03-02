class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1) # dp[0] = 0
        dp[1] = 0
        #dp[2] = min(cost[0], cost[1])
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]) 
        print(dp)
        return dp[-1]
