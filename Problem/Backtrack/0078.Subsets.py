class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            dfs(i+1) # Dose not choose, backtrack directly

            path.append(nums[i]) # Choose a num to add
            dfs(i+1)
            path.pop() # Recover

        if n > 0:
            dfs(0)
        return ans
        