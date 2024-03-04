class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums) % 2) == 1:
            return False # Fail to divide into two parts
        target = sum(nums) // 2 # the weight of the bag and the value of the object are equal to the target
        dp = [0] * (target+1) # dp[0] = 0
        for i in range(1, len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        if dp[-1] == target:
            return True
        return False
