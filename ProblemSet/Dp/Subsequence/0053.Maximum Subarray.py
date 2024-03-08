class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        
        #print(dp)
        return max(dp)
        '''
        # Greedy
        res = float("-inf")
        summa = 0
        for i in range(len(nums)):
            summa += nums[i]
            if summa > res:
                res = summa
            if summa < 0:
                summa = 0
        return res
        '''
