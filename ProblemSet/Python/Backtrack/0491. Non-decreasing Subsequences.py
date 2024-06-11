class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ret = []
        path = []
        def backtracking(startIdx):
            if len(path) >= 2:
                ret.append(path.copy()) # Does not return because we need all the valid nodes in the tree
            record = set() # record the number that has been used, use set that does not contain duplicated elements
            for i in range(startIdx, len(nums)):
                if len(path) > 0 and nums[i] < path[-1]:
                    continue
                if nums[i] in record:
                    continue
                path.append(nums[i])
                record.add(nums[i])
                backtracking(i+1)
                path.pop()
                # Does not need to remove the num[i] in record since it is recorded
        
        backtracking(0)
        return ret
    