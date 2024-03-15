class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = [0]
        for i in range(len(nums)*2):
            idx = i % len(nums)
            if nums[idx] <= nums[stack[-1]]:
                stack.append(idx)
            else:
                while stack and nums[idx] > nums[stack[-1]]:
                    res[stack[-1]] = nums[idx]
                    stack.pop()
                stack.append(idx)
        return res
