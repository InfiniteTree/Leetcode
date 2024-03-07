class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        path = []
        used = [False] * len(nums)
        nums.sort()
        def backtracking(startIdx):
            ret.append(path.copy())
            if startIdx > len(nums):
                return
            for i in range(startIdx, len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtracking(i+1)
                used[i] = False
                path.pop()
        backtracking(0)
        return ret
