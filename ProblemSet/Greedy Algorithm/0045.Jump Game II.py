class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        step = 0
        max_reachable = 0
        end_bound = 0 # point to the index that has jumped
        if n == 1:
            return step

        for i in range(n-1):
            max_reachable = max(max_reachable, i + nums[i])
            if i==end_bound:
                end_bound = max_reachable
                step += 1
        return step
        