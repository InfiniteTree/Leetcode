class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums) # the longest length
        count = [1] * len(nums) # the number of increasing subarray with the longest length
        max_length = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                    dp[i] = max(dp[i], dp[j]+1)
                max_length = max(max_length, dp[i])
        ret = 0
        for i in range(len(nums)):
            if dp[i] == max_length:
                ret += count[i]
        return ret
            