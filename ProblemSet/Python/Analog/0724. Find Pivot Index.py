class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left_s = 0
        for i,num in enumerate(nums):
            if left_s * 2 == s - num:
                return i
            left_s += num
        return -1
            