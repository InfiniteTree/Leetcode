class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for j in range(target+1):
            for num in nums:
                if j-num >= 0:
                    dp[j] += dp[j-num]
        #print(dp)
        return dp[-1]
