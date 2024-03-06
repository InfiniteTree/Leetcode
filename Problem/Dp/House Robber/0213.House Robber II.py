class Solution:
    def robLinear(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) == 1:
            return dp[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ret = max(self.robLinear(nums[:len(nums)-1]), self.robLinear(nums[1:len(nums)]))
        return ret
