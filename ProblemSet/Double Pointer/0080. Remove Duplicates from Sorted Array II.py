class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        p1, p2= 2, 2
        while p2 < len(nums):
            if nums[p2] != nums[p2-1] or (nums[p2] == nums[p1-1] and nums[p2] != nums[p1-2]):
                nums[p1] = nums[p2]
                p1 += 1
            p2 += 1
        return p1
        