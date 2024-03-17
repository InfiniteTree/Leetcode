class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, tot = 0, 0, 0
        minLen = inf
        while r < len(nums):
            tot += nums[r]
            while tot >= target:
                minLen = min(minLen, r-l+1)
                tot -= nums[l]
                l += 1
            r += 1
        return minLen if minLen != inf else 0
