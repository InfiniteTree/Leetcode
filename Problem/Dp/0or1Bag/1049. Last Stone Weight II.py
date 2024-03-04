class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        target = s // 2
        dp = [0] * (target + 1)
        for stone in stones:
            for j in range(target, stone-1, -1):
                dp[j] = max(dp[j], dp[j-stone]+stone)
        
        return s - dp[target] - dp[target] # Do not need abs() because a//2 <= a/2
        