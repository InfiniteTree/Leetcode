class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        suf[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suf[i] = min(suf[i+1], nums[i])
        
        res = inf
        pre = nums[0]
        for i in range(1, n-1):
            if pre < nums[i] > suf[i+1]:
                res = min(res, pre+nums[i]+suf[i+1])
            pre = min(pre, nums[i])
        return res if res != inf else -1
        