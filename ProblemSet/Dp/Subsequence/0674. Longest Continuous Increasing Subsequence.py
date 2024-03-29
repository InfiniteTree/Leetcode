class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        if len(nums) <= 1:
            return dp[len(nums)-1]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = max(dp[i], dp[i-1]+1)
        return max(dp)
