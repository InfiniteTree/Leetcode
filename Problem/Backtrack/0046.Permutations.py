class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        path = []
        used_t = [False] * len(nums)
        def backtracking(used):
            if len(path) == len(nums):
                ret.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i] == True:
                    continue
                path.append(nums[i])
                used[i] = True
                backtracking(used)
                path.pop()
                used[i] = False
        backtracking(used_t)
        return ret
        