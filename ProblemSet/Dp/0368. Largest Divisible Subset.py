class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n  # dp[i]: the length of the largest subset of nums[:i] that satisfies the requirement
        maxSize = 1
        maxVal = nums[0]
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)
            if dp[i] > maxSize:
                maxSize = dp[i]
                maxVal = nums[i]
        #print(dp)
        res = []
        for i in range(n-1, -1, -1):
            if dp[i] == maxSize and maxVal % nums[i] == 0:
                res.append(nums[i])
                maxVal = nums[i]
                maxSize -= 1
        return res
                