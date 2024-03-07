class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        # plusBag + subtractBag = sum , + plusBag - subtractBag = target
        # plusBag = (target + sum) / 2
        if (target + s) % 2 != 0: # Fail to form the target
            return 0
        if s < abs(target):
            return 0 
        plusBag = (target + s) // 2
        dp = [0] * (plusBag+1)
        dp[0] = 1
        for num in nums:
            for j in range(plusBag, num-1, -1):
                dp[j] += dp[j-num]
        return dp[-1]