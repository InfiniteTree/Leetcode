class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        count = n+1
        left = 0
        for right, x in enumerate(nums): # x == nums[right]
            s += x
            # Loop until when S>=target
            while s >= target:
                count = min(count, right-left+1) # update the subarrary
                s -= nums[left]
                left += 1
        return count if count <= n else 0
