class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []
        path = []
        used_t = [False] * len(nums)
        def backtracking(used):
            if len(path) == len(nums):
                ret.append(path.copy())
                return
            record = set()
            for i in range(len(nums)):
                if used[i] or nums[i] in record:
                    continue
                path.append(nums[i])
                used[i] = True
                record.add(nums[i])
                backtracking(used)
                used[i] = False
                path.pop()
        
        backtracking(used_t)
        return ret
    
        # Method 2, firstly we can sort the nums,
        # and then judge whether num[i] == num[i-1] when i > 0 in the for loop
        # in this method we do not need the set record!
