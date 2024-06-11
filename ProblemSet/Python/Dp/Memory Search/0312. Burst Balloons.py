class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        vals = [1] + nums + [1] # enlarge the array nums with the start 1 and end 1

        @cache
        def dfs(left: int, right: int) -> int:
            if left >= right - 1:
                return 0
            res = 0
            for i in range(left+1, right):
                tot = vals[left] * vals[i] * vals[right]
                tot += dfs(left, i) + dfs(i, right)
                res = max(res, tot)
            return res

        return dfs(0, n+1)
