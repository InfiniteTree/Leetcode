class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        path = []
        sum_t = 0
        def backtracking(startIdx, sum_t):
            if sum_t > target:
                return
            if sum_t == target:
                ret.append(path.copy())
                return
            for i in range(startIdx, len(candidates)):
                sum_t += candidates[i]
                path.append(candidates[i])
                backtracking(i, sum_t) # not i+1 because a number can be chosen an unlimited number of times
                path.pop()
                sum_t -= candidates[i]
        backtracking(0, sum_t)
        return ret
