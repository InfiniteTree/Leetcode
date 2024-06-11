class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = inf
        suf = [0] * n # suf[i]: min val in i to n-1
        suf[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suf[i] = min(suf[i+1], nums[i])
        pre = nums[0]
        for i in range(1, n-1):
            if pre < nums[i] > suf[i+1]:
                res = min(res, pre + nums[i] + suf[i+1])
            pre = min(pre, nums[i])
        '''
        pre = [0] * n # pre[i]: min val in 0 to i
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = min(pre[i-1], nums[i])
        
        for i in range(1, n-1):
            if pre[i-1] < nums[i] > suf[i+1]:
                res = min(res, pre[i-1] + nums[i] + suf[i+1])
        '''

        '''
        # Brust force
        for i in range(len(nums)-2):
            for j in range(i, len(nums)-1):
                for k in range(j, len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        res = min(res, nums[i]+nums[j]+nums[k])
        '''
        return res if res != inf else -1
